from flask import Flask, render_template, session, request, jsonify
import os

# --- ROBUST PATH CONFIGURATION ---
# This finds the location of THIS file and goes up one level to find templates/static
CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_FILE_DIR)

template_dir = os.path.join(ROOT_DIR, 'templates')
# We define static_dir even if empty, to prevent errors if you add files later
static_dir = os.path.join(ROOT_DIR, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = 'your_secret_key_here' 

# --- ROUTES FOR PAGES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signin')
def signin_page():
    return render_template('signin.html')

@app.route('/chemistry-course')
def chemistry_course():
    return render_template('Chemistry/AI_for_chem.html')

# --- AUTHENTICATION API ---

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # MOCK LOGIN: Accepts any non-empty email/password
    if email and password:
        session['user'] = email 
        return jsonify({"status": "success", "message": "Logged in via Python"})
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 400

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.json
    # MOCK REGISTER: Accepts any data
    if data.get('email'):
        session['user'] = data.get('email')
        return jsonify({"status": "success", "message": "Registered via Python"})
    else:
        return jsonify({"status": "error", "message": "Registration failed"}), 400

@app.route('/api/logout')
def api_logout():
    session.clear()
    return jsonify({"status": "success"})