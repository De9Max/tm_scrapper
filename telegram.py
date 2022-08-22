import requests

BOT_TOKEN = ""
BOT_CHAT_ID = ""


def send_notification(name, url):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                  json={"chat_id": BOT_CHAT_ID, "text": f"<b>NEW ARTICLE</b>\n<i>{name}</i>\n{url}",
                        "parse_mode": "HTML"})
