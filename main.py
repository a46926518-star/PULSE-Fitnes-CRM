from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == "admin@gmail.com" and password == "123456":
        return jsonify({"message": "Muvaffaqiyatli", "token": "maxfiy_token_123"}), 200
    else:
        return jsonify({"message": "Email yoki parol xato"}), 400


if __name__ == '__main__':
    app.run(port=5000, debug=True)