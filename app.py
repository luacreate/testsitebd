from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/postback:<int:id>:<action>', methods=['GET'])
def postback(id, action):
    # Здесь id будет целым числом, а action будет строкой (например, "REGISTRATION" или "DEPOSIT")
    data = {
        'id': id,
        'action': action
    }

    # Записываем данные в текстовый файл
    with open('postbacks.txt', 'a') as f:
        f.write(f"ID: {id}, Action: {action}\n")
    
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
