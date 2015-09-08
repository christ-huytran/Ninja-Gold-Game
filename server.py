from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = "'t\xef\xf0\xf0\x951\xf8\xf8\xa9\x16/$\xe4$<\xd3\x06\xf5\x95>s\xc8\xff"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money')
def process_money():
    return redirect(url_for('index'))

app.run(debug=True)
