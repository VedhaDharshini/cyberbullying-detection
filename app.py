from flask import Flask, request, jsonify
from utils.preprocess import preprocess_text
from utils.model import load_model, predict_label

app = Flask(__name__)
model = load_model()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    preprocessed = preprocess_text(text)
    label = predict_label(model, preprocessed)
    return jsonify({"prediction": label})

if __name__ == "__main__":
    app.run(debug=True)
