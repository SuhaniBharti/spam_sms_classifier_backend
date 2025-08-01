import nltk  
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import SMSRequest, SMSResponse
from app.predict import predict_message

app = FastAPI()


# origins = [
#     "http://localhost:5173", 
#     "https://spamdetection-gamma.vercel.app",  
#      "exp://*",             
#     "http://*",           
#     "https://*",           
#     "null" 
# ]
app.add_middleware(
    CORSMiddleware,
   allow_origin_regex=".*", 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "SMS Spam Classifier API is running."}


@app.post("/predict", response_model=SMSResponse)
def predict(data: SMSRequest):
    result = predict_message(data.text)
    return SMSResponse(prediction=result)
