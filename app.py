from flask import Flask, render_template
import urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/meta')
def meta():
    url = "http://169.254.169.254/latest/meta-data/"

    meta_list = urllib.request.urlopen(url).read().decode()
    str = "Metadata\n"
    for k in meta_list.split('\n'):
        url_with_key = url + k
        v = urllib.request.urlopen(url_with_key).read().decode()
        str = str + "%s is %s\n" % (k, v)
    return str

if __name__ == '__main__':
    app.run()
