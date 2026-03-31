# api/index.py
from flask import Flask
import os

# Configure template and static paths
template_dir = os.path.abspath('../templates')
static_dir = os.path.abspath('../static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return "Hello from Vercel! Flask is working."