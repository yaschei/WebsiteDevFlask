from flask import Flask, redirect, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/services', methods=['POST','GET'])
def services():
    return render_template("services.html")

@app.route('/publications', methods=['POST','GET'])
def publications():
    return render_template("publications.html")

@app.route('/about', methods=['POST','GET'])
def about():
    return render_template("resume.html")

@app.route('/contact', methods=['POST','GET'])
def contact():
    return render_template("contact.html")

@app.route('/acknowledgments', methods=['POST','GET'])
def acknowledgments():
    return render_template("acknowledgments.html")
