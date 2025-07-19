from fastapi import FastAPI, Request
import telegram
import os

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN") or "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"
bot = telegram.Bot(token=BOT_TOKEN)

@app.get("/")
def root():
    return {"message": "Telegram bot running"}

@app.post("/webhook/{token}")
async def telegram_webhook(request: Request, token: str):
    if token != BOT_TOKEN:
        return {"error": "Invalid token"}

    data = await request.json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text.strip() == "/run":
            bot.send_message(chat_id=chat_id, text="📈 전략 실행 시작!")
            # 여기에 전략 실행 코드 삽입 가능
        else:
            bot.send_message(chat_id=chat_id, text="🤖 명령어를 인식하지 못했습니다.")

    return {"status": "ok"}

