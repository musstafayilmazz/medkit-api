from fastapi import FastAPI
from pydantic import BaseModel
from eMail import email_send
from datetime import datetime, timedelta, timezone

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

@app.get("/get_time")
def get_turkey_time():
    tz = timezone(timedelta(hours=3))  # Türkiye saat dilimi
    now = datetime.now(tz)
    return {"turkey_time": now.strftime("%Y-%m-%d %H:%M:%S")}