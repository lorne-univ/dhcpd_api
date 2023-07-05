#!/usr/bin/env python3

from flask import Flask, jsonify, request, __version__
import re


app = Flask(__name__)
print(f"Flask : {__version__}")


# Pour lancer le service : flask run --host=0.0.0.0
# Pour tester : curl -X POST http://fog-z220.local.univ-savoie.fr:5000 -H 'Content-Type: application/json' -d '{"mac_address":"00:80:C1:B2:D3:E3"}'
@app.route("/", methods=["POST"])
def index():
    mac_address = request.json["mac_address"]
    with open("/var/log/messages") as messages:
        messages_content = messages.read()
        messages.close()
    ip_addr = re.search(r"(?i)DHCPACK on (.*) to " + mac_address, messages_content)
    if ip_addr:
        return f"{ip_addr.group(1)}"
    else:
        return "None"
