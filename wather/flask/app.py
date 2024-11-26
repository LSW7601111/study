from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def lsw1():
    return render_template('index.html')

@app.route('/keyboard')
def keyboard():
    return render_template('keyboard.html')

if __name__ =='__main__':
    app.run('0.0.0.0', port=5000, debug=True)