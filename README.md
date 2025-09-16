# Whatsapp_TalkShield
Talkshield_Bot for whatsapp moderation

# WhatsApp Moderation Bot

This bot connects WhatsApp (via Twilio) to a Hugging Face moderation model
([Sekhinah/Talk_Shield](https://huggingface.co/Sekhinah/Talk_Shield)).

## Features
- Receives WhatsApp messages via Twilio webhook.
- Sends text to Hugging Face Space for toxicity classification.
- Replies with flagged categories or marks as safe.

## Deployment
1. Fork or clone this repo.
2. Set your environment variables on Render:
   - `HF_TOKEN` = your Hugging Face API token.
3. Deploy as a **Web Service**.

## Local Development
```bash
pip install -r requirements.txt
export HF_TOKEN=your_token
flask run --port=5000
