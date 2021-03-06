from flask import Flask, render_template, request

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/index.html")
def Home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/works.html")
def works():
    return render_template('works.html')
