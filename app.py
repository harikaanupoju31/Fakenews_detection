from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = None
vectorizer = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    global model, vectorizer

    if model is None:
        model = pickle.load(open("model.pkl", "rb"))
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    data = request.get_json()
    text = data["text"]

    vect = vectorizer.transform([text])
    prediction = model.predict(vect)[0]

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run()
