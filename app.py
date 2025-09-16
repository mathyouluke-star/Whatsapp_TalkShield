from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests, os

HF_URL = "https://api-inference.huggingface.co/models/Sekhinah/Talk_Shield"
HF_HEADERS = {"Authorization": f"Bearer " + os.environ.get("HF_TOKEN")}

app = Flask(__name__)

SPACE_URL = "https://Sekhinah-talkshield-api.hf.space"

def check_toxicity(text: str):
    try:
        # send input to your Space
        r = requests.post(SPACE_URL, json={"data": [text]}, timeout=60)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e), "raw": getattr(r, "text", "")}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    msg = request.form.get("Body", "")
    sender = request.form.get("From", "")

    result = check_toxicity(msg)
    reply = MessagingResponse()

    if "error" in result:
        reply.message(f"⚠️ Space error: {result['error']}")
    else:
        # Space returns {"data": [ ... ]}
        predictions = result.get("data", [{}])[0]
        flagged = [k for k, v in predictions.items() if v > 0.3]

        if flagged:
            reply.message(f"⚠️ Message flagged for: {', '.join(flagged)}")
        else:
            reply.message("✅ Message looks fine!")

    return str(reply)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
