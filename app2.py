from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!\n'
    
@app.route('/info')
def info():
    return 'Infomation page\n'
