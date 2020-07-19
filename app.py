from flask import Flask, render_template
import urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/meta/<key>')
def meta():
    url = "http://169.254.169.254/latest/meta-data/" + key

    ret = urllib.request.urlopen(url).read().decode()
    return "Metadata %s is %s\n" % (key, ret)

if __name__ == '__main__':
    app.run()