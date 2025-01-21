from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from typing import List, Any, Dict
import numpy as np

class BugBountyModel:
    def __init__(self):
        self.pipeline = Pipeline([
            ('vectorizer', TfidfVectorizer(max_features=10000)),
            ('classifier', LogisticRegression(max_iter=1000))
        ])

    def train(self, texts: List[str], labels: List[Any]) -> Dict[str, float]:
        """Train the model and return metrics."""
        self.pipeline.fit(texts, labels)
        
        # Calculate training metrics
        predictions = self.pipeline.predict(texts)
        accuracy = np.mean(predictions == labels)
        
        return {
            'accuracy': accuracy
        }

    def predict(self, texts: List[str]) -> List[int]:
        """Make predictions on new texts."""
        return self.pipeline.predict(texts)

    def predict_proba(self, texts: List[str]) -> List[List[float]]:
        """Get prediction probabilities for each class."""
        return self.pipeline.predict_proba(texts)

    def save_model(self, file_path: str):
        """Save the trained model to disk."""
        joblib.dump(self.pipeline, file_path)

    def load_model(self, file_path: str):
        """Load a trained model from disk."""
        self.pipeline = joblib.load(file_path)