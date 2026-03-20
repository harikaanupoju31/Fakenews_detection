# model.py

import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -----------------------------
# 1. Create Dataset
# -----------------------------
data = {
    "text": [
        # Real News (1)
        "Government passes new education policy",
        "Stock market reaches new high today",
        "Scientists discover new species in forest",
        "New technology improves healthcare system",
        "India launches new satellite successfully",

        # Fake News (0)
        "Aliens landed in India yesterday",
        "Government gives free laptops to everyone without rules",
        "Drinking 10 cups of coffee guarantees success",
        "Students will pass exams without studying",
        "Time machine invented by college students"
    ],
    "label": [
        1, 1, 1, 1, 1,   # Real
        0, 0, 0, 0, 0    # Fake
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Split Data
# -----------------------------
X = df["text"]
y = df["label"]

# -----------------------------
# 3. Convert Text → Numbers
# -----------------------------
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# -----------------------------
# 4. Train Model
# -----------------------------
model = LogisticRegression()
model.fit(X_vectorized, y)

# -----------------------------
# 5. Save Model & Vectorizer
# -----------------------------
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved successfully!")