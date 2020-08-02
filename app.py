from flask import Flask, render_template
import urllib.request
import os

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

    metadata_list = urllib.request.urlopen(url).read().decode()
    str = "Metadata\n"
    for k in metadata_list.split('\n'):
        url_with_key = url + k
        v = urllib.request.urlopen(url_with_key).read().decode()
        str = str + "%s is %s\n" % (k, v)
    return str

@app.route('/load')
def load():
    idleCpu = int(os.popen('vmstat 1 2 | awk \'{ for (i=1; i<=NF; i++) if ($i=="id") { getline; getline; print $i }}\'').read())
    
    if idleCpu > 50:
        os.system('dd if=/dev/zero bs=100M count=500 | gzip | gzip -d  > /dev/null &')
        return '<p>Current CPU load is %s</p><p>Generating CPU Load!</p>' % str(100 - idleCpu)
    else:
        return '<p>Current CPU load is %s</p><p>Under High CPU Load!</p>' % str(100 - idleCpu)
        
if __name__ == '__main__':
    app.run()
