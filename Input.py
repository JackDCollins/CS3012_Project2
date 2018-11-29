from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
