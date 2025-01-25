from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Basic user management
users = {} 

def register_user(username, password):
    users[username] = generate_password_hash(password)

def verify_user(username, password):
    return username in users and check_password_hash(users[username], password)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        register_user(username, password)
        return jsonify({"message": "User registered"}), 201
    
    return jsonify({"error": "Invalid credentials"}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if verify_user(username, password):
        return jsonify({"message": "Login successful"}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/')
def home():
    return render_template('index.html', message='Hello, DevSecOps!')

if __name__ == '__main__':
    app.run(debug=True)
