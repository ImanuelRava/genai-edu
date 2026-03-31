# api/index.py
from flask import Flask, render_template, send_file, session, request, jsonify
import os

template_dir = os.path.abspath('../templates')
static_dir = os.path.abspath('../static')

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

    if email and password:
        session['user'] = email 
        return jsonify({"status": "success", "message": "Logged in via Python"})
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 400

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.json
    session['user'] = data.get('email')
    return jsonify({"status": "success", "message": "Registered via Python"})

@app.route('/api/logout')
def api_logout():
    session.clear()
    return jsonify({"status": "success"})

# --- FILE SERVING ---

@app.route('/api/file/<filename>')
def serve_file(filename):
    if 'user' not in session:
        return "You must be logged in to download this file.", 401
    
    try:
        file_path = os.path.join(static_dir, 'chemistry_pdfs', filename)
        return send_file(file_path)
    except FileNotFoundError:
        return "File not found", 404