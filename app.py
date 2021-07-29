from flask import Flask, app, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Register')
def register():
    return render_template('Register.html')

if __name__ == "__app__":
    app.run(debbug=True)