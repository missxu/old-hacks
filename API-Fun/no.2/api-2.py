from flask import Flask
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("APril API No. 2 - integration with Twilio - what fun!")
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
