from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Hello_world():
    return render_template('index.html')

@app.route('/home')
def Home():
    return "this is home page"

if __name__ == '__main__':
    app.run(debug = True)
