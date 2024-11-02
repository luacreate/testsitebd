from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/postback', methods=['POST'])
def postback():
    data = request.json  # Получи данные из postback запроса
    # Записываем данные в текстовый файл
    with open('postbacks.txt', 'a') as f:  # Открываем файл в режиме добавления
        f.write(str(data) + '\n')  # Записываем данные и переводим строку
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
