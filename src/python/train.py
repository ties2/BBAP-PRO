from data_processor import DataProcessor
from model import BugBountyModel
import json
import os

def main():
    # Create output directories if they don't exist
    os.makedirs('models', exist_ok=True)
    
    # Initialize processor and model
    processor = DataProcessor()
    model = BugBountyModel()
    
    # Load and preprocess data
    print("Loading and preprocessing data...")
    data = processor.load_data('data/training_data.json')
    
    # Save label mappings
    processor.save_label_maps('models/label_maps.json')
    
    # Train model
    print("Training model...")
    metrics = model.train(data['texts'], data['labels'])
    
    # Save model
    print("Saving model...")
    model.save_model('models/bug_bounty_model.joblib')
    
    # Save training metrics
    with open('models/training_metrics.json', 'w') as f:
        json.dump(metrics, f)
    
    print(f"Training completed! Accuracy: {metrics['accuracy']:.2%}")

if __name__ == "__main__":
    main()