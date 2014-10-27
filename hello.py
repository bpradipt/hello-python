import os
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    #print the request Body
    print request.values.get('Body')
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Hello, This is Pradipta's Twilio Acc")
    return str(resp)

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
