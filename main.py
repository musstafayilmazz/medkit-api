from fastapi import FastAPI
from pydantic import BaseModel
from eMail import email_send

app = FastAPI()

class EmailRequest(BaseModel):
    apikey: str
    body: str
    subject: str
    receiver: str


@app.get("/")
async def root():
    return {"message": "Welcome To Api"}



@app.post("/send_email")
async def send_email(email_request: EmailRequest):
    apikey = email_request.apikey
    body = email_request.body
    subject = email_request.subject
    receiver = email_request.receiver

    try:
        email_send(apikey,body,subject,receiver)
        return {"message": "E-mail sent!"}
    except:
        return {"message": "Unauth access!"}