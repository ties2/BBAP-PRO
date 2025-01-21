from data_processor import DataProcessor
from model import BugBountyModel
import sys
import json

def main():
    # Check if input text is provided
    if len(sys.argv) < 2:
        print("Usage: python predict.py 'vulnerability description'")
        sys.exit(1)
    
    input_text = sys.argv[1]
    
    # Initialize processor and model
    processor = DataProcessor()
    model = BugBountyModel()
    
    # Load label mappings and model
    processor.load_label_maps('models/label_maps.json')
    model.load_model('models/bug_bounty_model.joblib')
    
    # Preprocess input
    processed_text = processor.preprocess_text(input_text)
    
    # Make prediction
    prediction = model.predict([processed_text])[0]
    probabilities = model.predict_proba([processed_text])[0]
    
    # Get original label
    predicted_label = processor.decode_labels([prediction])[0]
    
    # Prepare results
    result = {
        'input_text': input_text,
        'predicted_category': predicted_label,
        'confidence': float(max(probabilities))
    }
    
    # Print results
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()