# Phishing Email Detection Model

## Objective
Build a machine-learning classifier using Scikit-learn to classify emails as **Phishing** or **Safe**.

## Features
- TF-IDF text features
- URL count feature
- Suspicious-keyword count feature
- Logistic Regression classifier
- Accuracy and classification report
- Confusion matrix
- Interactive email prediction

## Run on Windows

1. Install Python 3.10+.
2. Open Command Prompt in this project folder.
3. Install libraries:
   `pip install -r requirements.txt`
4. Run:
   `python train_model.py`

A confusion-matrix image will be saved in `outputs/confusion_matrix.png`.

## Important
The included `data/emails.csv` is a small educational/demo dataset so the project can run immediately. For a stronger real-world submission, replace it with a larger verified phishing/legitimate email dataset while keeping the columns `text` and `label`.

## Technologies
Python, Pandas, Scikit-learn, TF-IDF, Logistic Regression, Matplotlib.
