from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained machine learning model
with open('models/vulnerability_classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_vulnerability():
    if request.method == 'POST':
        description = request.form['description']
        
        # Predict the vulnerability category
        prediction = model.predict([description])[0]
        
        return render_template('index.html', prediction=prediction, description=description)

if __name__ == '__main__':
    app.run(debug=True)
