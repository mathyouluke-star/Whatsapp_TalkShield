from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests, os

HF_URL = "https://api-inference.huggingface.co/models/Sekhinah/Talk_Shield"
HF_HEADERS = {"Authorization": f"Bearer " + os.environ.get("HF_TOKEN")}

app = Flask(__name__)

def check_toxicity(text: str):
    r = requests.post(HF_URL, headers=HF_HEADERS, json={"inputs": text})
    try:
        return r.json()
    except Exception:
        return {"error": r.text, "status": r.status_code}


@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    msg = request.form.get("Body", "")
    sender = request.form.get("From", "")

    result = check_toxicity(msg)

    # filter labels above 0.3 threshold
    flagged = [k for k,v in result[0].items() if v > 0.3]

    resp = MessagingResponse()
    if flagged:
        resp.message(f"⚠️ Message flagged for: {', '.join(flagged)}")
    else:
        resp.message("✅ Message looks fine!")

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
