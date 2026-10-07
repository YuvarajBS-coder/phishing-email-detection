import re
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Dataset
df = pd.read_csv("data/emails.csv")

def enrich_text(text):
    text = str(text).lower()

    url_count = len(
        re.findall(r"https?://\S+|www\.\S+", text)
    )

    suspicious_words = [
        "urgent", "verify", "password", "pin",
        "otp", "click", "claim", "prize",
        "winner", "suspended", "blocked",
        "refund", "fee", "cvv", "login"
    ]

    keyword_count = sum(
        text.count(word) for word in suspicious_words
    )

    return text + f" URLS_{url_count} SUSPICIOUS_{keyword_count}"


# Prepare data
X = df["text"].apply(enrich_text)
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create model
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )
    ),
    (
        "classifier",
        LogisticRegression(max_iter=1000)
    )
])

# Train
model.fit(X_train, y_train)

# Test
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n======================================")
print("     PHISHING EMAIL DETECTION MODEL")
print("======================================")

print("Dataset size :", len(df))
print("Training rows:", len(X_train))
print("Testing rows :", len(X_test))

print(f"\nAccuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)

# Confusion Matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=["Safe", "Phishing"]
)

print("Confusion Matrix:")
print(cm)

print("\nRows = Actual")
print("Columns = Predicted")
print("          Safe  Phishing")
print(f"Safe      {cm[0][0]}      {cm[0][1]}")
print(f"Phishing  {cm[1][0]}      {cm[1][1]}")


# Automatic phishing test
phishing_email = """
URGENT! Your bank account will be suspended.
Verify your password immediately at
http://secure-login.example
"""

result1 = model.predict(
    [enrich_text(phishing_email)]
)[0]

print("\nTest Email 1:")
print("URGENT bank account verification email")
print("Prediction:", result1)


# Automatic safe test
safe_email = """
Your university assignment submission deadline
is tomorrow. Please submit your report.
"""

result2 = model.predict(
    [enrich_text(safe_email)]
)[0]

print("\nTest Email 2:")
print("University assignment reminder")
print("Prediction:", result2)

print("\n======================================")
print("       PROJECT COMPLETED SUCCESSFULLY")
print("======================================")