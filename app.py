from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    msg = request.form.get('Body', '').strip().lower()
    resp = MessagingResponse()

    if msg == "1":
        resp.message("ممتاز! درس 1: أحكام النون الساكنة. اكتب 2 للدرس التالي.")
    elif msg == "2":
        resp.message("درس 2: أحكام الميم الساكنة. اكتب 1 للرجوع.")
    else:
        resp.message("اهلا بكم في بوت التجويد \nاكتب 1 للبدء")
    
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
