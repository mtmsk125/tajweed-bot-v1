from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
import os

app = Flask(__name__)

# 1. حط المتون هون. زيد براحتك
MUTUN = {
    "1": {"name": "تحفة الاطفال", "abyat": [
        "يقول راجي رحمة الغفور",
        "دوما سليمان هو الجمزوري",
        "الحمد لله مصليا على",
        "محمد واله ومن تلا"
    ]} # كمل باقي الـ 61 بيت هون
}

DATA_FILE = "progress.json"

def load_progress():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE) as f:
        return json.load(f)

def save_progress(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    num = request.form['From']
    msg = request.form['Body'].strip()
    progress = load_progress()

    if num not in progress:
        progress[num] = {"mutn": None, "index": 0}

    user = progress[num]
    resp = MessagingResponse()
    text = ""

    if msg == "ابدأ" or user["mutn"] is None:
        text = "السلام عليكم \nاختار متن:\n1- تحفة الاطفال\nاكتب رقم"

    elif msg == "1" and user["mutn"] is None:
        user["mutn"] = "1"
        user["index"] = 0
        text = f"تمام بلشنا تحفة \n\nالبيت 1:\n{MUTUN['1']['abyat'][0]}\n\nاكتب: تم"

    elif msg.lower() == "تم":
        user["index"] += 1
        if user["index"] >= len(MUTUN[user["mutn"]]["abyat"]):
            text = "مبروك ختمت الابيات اللي موجودة \nاكتب ابدأ عشان تعيد"
            user["mutn"] = None
        else:
            text = f"البيت {user['index']+1}:\n{MUTUN[user['mutn']]['abyat'][user['index']]}\n\nاكتب: تم"
    else:
        text = "اكتب: تم لما تحفظ البيت\nاو ابدأ للبداية"

    save_progress(progress)
    resp.message(text)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
