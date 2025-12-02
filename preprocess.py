from langdetect import detect

def preprocess_text(text):
    return text.lower()

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"
