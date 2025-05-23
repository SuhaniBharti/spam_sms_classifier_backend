import pickle
import string
from nltk.corpus import stopwords
from pathlib import Path

def remove_punctuation_and_stopwords(sms):
    sms_no_punctuation = [ch for ch in sms if ch not in string.punctuation]
    sms_no_punctuation = "".join(sms_no_punctuation).split()
    return [word.lower() for word in sms_no_punctuation if word.lower() not in stopwords.words("english")]


import __main__
__main__.remove_punctuation_and_stopwords = remove_punctuation_and_stopwords


model_path = Path(__file__).parent.parent / "model" / "message classifier model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

def predict_message(text: str) -> str:
    return model.predict([text])[0]
