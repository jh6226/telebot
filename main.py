# main.py

from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()
BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
def root():
    return {"message": "Telegram bot is running!"}

@app.post(f"/webhook/{BOT_TOKEN}")
async def webhook(request: Request):
    data = await request.json()
    # 명령어 처리 로직 (예: /start, /signal 등)
    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": text})
