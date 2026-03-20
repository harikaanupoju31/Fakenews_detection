from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "Fake News Detection API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    news = data["text"]

    transformed = vectorizer.transform([news])
    prediction = model.predict(transformed)[0]

    result = "Real News" if prediction == 1 else "Fake News"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)