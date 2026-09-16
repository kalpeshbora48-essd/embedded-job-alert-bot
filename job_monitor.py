
import os
import requests


BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
        },
        timeout=20,
    )

    response.raise_for_status()


if __name__ == "__main__":
    send_telegram(
        "✅ NEW EMBEDDED JOB BOT IS CONNECTED!\n\n"
        "The new monitoring system is ready for source integration."
    )

    print("Telegram test message sent successfully.")
