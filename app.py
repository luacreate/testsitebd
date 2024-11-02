from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/postback', methods=['POST'])
def postback():
    data = request.json  # Получи данные из postback запроса
    # Записываем данные в текстовый файл
    with open('postbacks.txt', 'a') as f:  # Открываем файл в режиме добавления
        f.write(str(data) + '\n')  # Записываем данные и переводим строку
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Используем переменную окружения PORT
    app.run(host='0.0.0.0', port=port)
