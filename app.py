from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]

    return jsonify({'prediction': str(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
