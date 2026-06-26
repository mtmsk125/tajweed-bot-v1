from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    print(">>> وصلت رسالة من واتساب <<<")
    resp = MessagingResponse()
    resp.message("البوت شغال 100% وصلت رسالتك")
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
 
      
