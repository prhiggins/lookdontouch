from ipaddress import ip_address, ip_network
import ipaddress

from flask import Flask, render_template, request

app = Flask(__name__)

def is_reserved(address):
    ip = ip_address(address)

    networks = [
    '0.0.0.0/8',
    '10.0.0.0/8',
    '100.64.0.0/10',
    '127.0.0.0/8',
    '169.254.0.0/16',
    '172.16.0.0/12',
    '192.0.0.0/24',
    '192.0.2.0/24',
    '192.168.0.0/16',
    '198.18.0.0/15']

    result = False
    for mask in networks:
        result |= ip in ip_network(mask)
    
    return result

@app.route("/")
def index():

    ip = None
    route = request.access_route
    for address in route:
        if not is_reserved(address):
            ip = address

    return render_template("index.html", visitor_ip=ip)