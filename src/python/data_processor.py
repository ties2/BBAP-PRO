import re
from typing import List, Dict, Any
import json

class DataProcessor:
    def __init__(self):
        self.label_map = {}
        self.reverse_label_map = {}

    def preprocess_text(self, text: str) -> str:
        """Clean and normalize text data."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters
        text = text.replace("'", "'").replace("–", "-")
        # Convert to lowercase
        text = text.lower()
        return text.strip()

    def encode_labels(self, labels: List[str]) -> List[int]:
        """Convert string labels to numeric indices."""
        unique_labels = sorted(set(labels))
        self.label_map = {label: idx for idx, label in enumerate(unique_labels)}
        self.reverse_label_map = {idx: label for label, idx in self.label_map.items()}
        return [self.label_map[label] for label in labels]

    def decode_labels(self, encoded_labels: List[int]) -> List[str]:
        """Convert numeric indices back to string labels."""
        return [self.reverse_label_map[label] for label in encoded_labels]

    def load_data(self, file_path: str) -> Dict[str, List[Any]]:
        """Load and preprocess training data from JSON file."""
        with open(file_path, 'r') as f:
            raw_data = json.load(f)
            data = raw_data['data']  # Access the 'data' array from the JSON
        
        texts = [self.preprocess_text(item['description']) for item in data]
        labels = [item['category'] for item in data]
        encoded_labels = self.encode_labels(labels)
        
        return {
            'texts': texts,
            'labels': encoded_labels,
            'original_labels': labels
        }

    def save_label_maps(self, file_path: str):
        """Save label mappings to file."""
        with open(file_path, 'w') as f:
            json.dump({
                'label_map': self.label_map,
                'reverse_label_map': self.reverse_label_map
            }, f)

    def load_label_maps(self, file_path: str):
        """Load label mappings from file."""
        with open(file_path, 'r') as f:
            maps = json.load(f)
            self.label_map = maps['label_map']
            self.reverse_label_map = maps['reverse_label_map']