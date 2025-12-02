import joblib

def load_model():
    return joblib.load("model/cyberbullying_model.pkl")

def predict_label(model, text):
    return model.predict([text])[0]
