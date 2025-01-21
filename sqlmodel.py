import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# Path to the dataset generated from sqldataset.py
DATASET_FILE = 'sql_injection_dataset.csv'

# Verify dataset existence
if not os.path.exists(DATASET_FILE):
    raise FileNotFoundError(f"Dataset file {DATASET_FILE} not found. Run sqldataset.py to generate it.")

# Load the dataset from the CSV file
df = pd.read_csv(DATASET_FILE)

# Validate the structure of the dataset
required_columns = {'query', 'label'}
if not required_columns.issubset(df.columns):
    raise ValueError(f"Dataset must contain the following columns: {required_columns}")

# Features and labels
X = df['query']          # SQL queries
y = df['label']          # Labels: 1 (malicious), 0 (legitimate)

# Check the distribution of classes
print("Class distribution in the dataset:")
print(y.value_counts())

# Split the data into train and test sets (maintain class distribution using stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Print class distribution in train and test sets
print("\nClass distribution in the training set:")
print(y_train.value_counts())

print("\nClass distribution in the test set:")
print(y_test.value_counts())

# Machine learning pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),  # Convert text to numerical features
    ('classifier', LogisticRegression(max_iter=1000))  # Logistic Regression classifier
])

# Train the model
pipeline.fit(X_train, y_train)

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Save the trained model
model_path = 'models/sql_injection_classifier.pkl'
with open(model_path, 'wb') as model_file:
    pickle.dump(pipeline, model_file)

print(f'\nTrained model saved at {model_path}')

# Evaluate the model
accuracy = pipeline.score(X_test, y_test)
print(f'\nModel accuracy on test set: {accuracy * 100:.2f}%')

# Optionally test the model with new input (example)
print("\nTesting the model with new queries:")
test_queries = [
    "SELECT * FROM users WHERE username='admin';",  # Legitimate
    "' OR '1'='1; DROP TABLE users; --",           # Malicious
    "SELECT email FROM customers WHERE id='101';"  # Legitimate
]

# Predict
predictions = pipeline.predict(test_queries)
for query, prediction in zip(test_queries, predictions):
    label = "Malicious" if prediction == 1 else "Legitimate"
    print(f"Query: {query}\nPrediction: {label}\n")
