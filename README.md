# Bug Bounty Model Training Pipeline

This project implements a machine learning pipeline for training models on bug bounty vulnerability reports. It includes data preprocessing, model training, and prediction capabilities.

## Project Structure

```
.
├── data/
│   └── training_data.json    # Training data in JSON format
├── src/
│   └── python/
│       ├── data_processor.py # Data preprocessing utilities
│       ├── model.py          # ML model implementation
│       ├── train.py         # Training script
│       ├── predict.py       # Prediction script
│       └── requirements.txt  # Python dependencies
└── models/                   # Directory for saved models (created during training)
```

## Setup

1. Install Python dependencies:
```bash
pip install -r src/python/requirements.txt
```

2. Prepare your training data in `data/training_data.json` following the example format.

## Usage

### Training

To train the model:

```bash
npm run train
```

This will:
- Load and preprocess the training data
- Train the model
- Save the model and label mappings to the `models/` directory
- Output training metrics

### Making Predictions

To make predictions on new vulnerability descriptions:

```bash
npm run predict "Your vulnerability description here"
```

The output will be a JSON object containing:
- The input text
- Predicted vulnerability category
- Confidence score

## Data Format

Training data should be in JSON format with the following structure:

```json
{
  "data": [
    {
      "description": "Vulnerability description",
      "category": "vulnerability_type"
    }
  ]
}
```

## Model Details

The current implementation uses:
- TF-IDF vectorization for text features
- Logistic Regression for classification
- Scikit-learn Pipeline for end-to-end processing

## Contributing

Feel free to submit issues and enhancement requests!