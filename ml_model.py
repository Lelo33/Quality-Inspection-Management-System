"""Defect prediction model for the Quality Inspection Management System.

Trains a logistic regression classifier on SIMULATED inspection data and
reports accuracy, precision and recall on a held-out test set.
"""
import random

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


def make_sample_data(n=500, seed=42):
    """Simulate inspections. Features: [deviation from target, line speed, temperature]."""
    rng = random.Random(seed)
    X, y = [], []
    for _ in range(n):
        deviation = rng.gauss(0, 1.2)
        speed = rng.gauss(100, 8)
        temp = rng.gauss(70, 5)
        risk = 1.4 * abs(deviation) + 0.03 * (speed - 100) + 0.05 * (temp - 70)
        defect = 1 if risk + rng.gauss(0, 0.5) > 1.6 else 0
        X.append([deviation, speed, temp])
        y.append(defect)
    return X, y


def train_and_evaluate():
    """Train with a train/test split and return the model and its metrics."""
    X, y = make_sample_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    metrics = {
        "accuracy": round(accuracy_score(y_test, predictions), 2),
        "precision": round(precision_score(y_test, predictions), 2),
        "recall": round(recall_score(y_test, predictions), 2),
    }
    return model, metrics


def predict_defect_probability(model, deviation, speed, temp):
    """Probability (0 to 1) that an inspection with these readings is a defect."""
    return float(model.predict_proba([[deviation, speed, temp]])[0][1])


if __name__ == "__main__":
    _, metrics = train_and_evaluate()
    print("Defect prediction model (simulated data)")
    print(metrics)