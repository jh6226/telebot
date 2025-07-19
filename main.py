from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "8047919145:AAH0LvACJLKD1BzdJOs52KsC2WGoYFcNQfo"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.post(f"/webhook/{BOT_TOKEN}")
async def telegram_webhook(req: Request):
    body = await req.json()

    if "message" in body:
        chat_id = body["message"]["chat"]["id"]
        text = body["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "✅ 봇이 정상적으로 연결되었습니다!")
        elif text == "/signal":
            send_message(chat_id, "📡 신호 요청을 수신했습니다. (여기에 로직 연결 예정)")
        else:
            send_message(chat_id, "🤖 지원되지 않는 명령어입니다.")

    return {"ok": True}


def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)
