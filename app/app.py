from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    ip = request.remote_addr
    return render_template("index.html", visitor_ip=ip)