from flask import Flask, request
import requests
import json

app = Flask(__name__)

BOT_TOKEN = "7660405983:AAFx18ZZGA16MtED4nk_X_TnwZjB-HYYoWM"
CHAT_ID = "1481262314"

TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        message = data.get('message', 'New Alert from TradingView')
        
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        
        response = requests.post(TELEGRAM_URL, json=payload)
        
        if response.status_code == 200:
            return {'status': 'success'}, 200
        else:
            return {'status': 'error'}, 400
            
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
