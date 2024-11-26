# 1. 플라스크를 인스톨 해서 설치해 줍니다. pip install flask
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def lsw1():
    return render_template('index.html')

if __name__ =='__main__':
    app.run('0.0.0.0', port=5000, debug=True)