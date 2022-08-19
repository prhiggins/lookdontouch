from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    return render_template("index.html", visitor_ip=ip)