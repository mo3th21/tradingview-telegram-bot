from flask import Flask, request
import requests

app = Flask(__name__)

# ضع هنا بياناتك
TELEGRAM_TOKEN = "7660405983:AAFx18ZZGA16MtED4nk_X_TnwZjB-HYYoWM"
CHAT_ID = "1481262314"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', '🚨 New Trading Signal Received')
    
    # إرسال الرسالة إلى Telegram
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)
    
    return "✅ Message Sent to Telegram!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
