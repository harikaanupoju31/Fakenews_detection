from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle

app = Flask(__name__, static_folder='.')
CORS(app)   # 👈 IMPORTANT LINE

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]

    if prediction == 1:
        result = "Real News"
    else:
        result = "Fake News"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
