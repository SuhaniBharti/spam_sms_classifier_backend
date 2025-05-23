from pydantic import BaseModel

class SMSRequest(BaseModel):
    text: str

class SMSResponse(BaseModel):
    prediction: str
