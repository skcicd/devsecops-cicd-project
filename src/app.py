from flask import Flask, request, jsonify, render_template, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Use a strong, random secret key

# In-memory user storage (replace with database in production)
users = {}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')
        
        if username in users:
            return jsonify({"error": "User already exists"}), 400
        
        users[username] = generate_password_hash(password)
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')
        
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect('/')
        
        return jsonify({"error": "Invalid credentials"}), 401
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/')
@login_required
def home():
    return render_template('index.html', message=f'Hello, {session["username"]}!')

if __name__ == '__main__':
    app.run(debug=True)