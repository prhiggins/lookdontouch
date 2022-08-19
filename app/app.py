from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.access_route[0]

    return render_template("index.html", visitor_ip=ip)