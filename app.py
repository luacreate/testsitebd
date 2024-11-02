from flask import Flask, request, jsonify
import os
import re

app = Flask(__name__)

@app.route('/postback/<path:action>', methods=['GET', 'POST'])  # Обработка всех GET и POST запросов
def postback(action):
    # Извлекаем ID и действие из URL
    match = re.match(r'(\d+):(.+)', action)
    if match:
        id = match.group(1)
        action_type = match.group(2)

        # Записываем данные в текстовый файл
        with open('postbacks.txt', 'a') as f:
            f.write(f"ID: {id}, Action: {action_type}\n")

        return jsonify({'status': 'success', 'data': {'id': id, 'action': action_type}})
    
    return jsonify({'status': 'error', 'message': 'Invalid format'}), 400

@app.route('/')
def home():
    return "Server is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
