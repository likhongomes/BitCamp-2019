# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)
account_sid = 'ACf797a6b1926d1b042838e6823133f2ab'
auth_token = 'bd035778a88f156ed5a40acefb612c3a'

client = Client(account_sid, auth_token)


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    message = client.messages.list()
    print(message[0].body)
    # Add a message
    text = "SchBoi! Your message is " + message[0].body
    resp.message(text)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
