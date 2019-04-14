from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import socket, time
client_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    print("ASDASD")
    # client_socket.bind(('localhost', 3207))
    # client_socket.listen()
    # conn, addr = client_socket.accept()
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    # print('Connected by', addr)        
    resp = MessagingResponse()
    # obbtains phone number of the client
    number = request.form['From']
    # obtains the text message from the client
    message_body = request.form['Body']     
    # conn.sendall(str(message_body))
    # time.sleep(9)
    # data = conn.recv(512)
    # print(data)
    # resp.message(data)
    resp.message("Ahoy! Thanks so much for your message.")
    print(message_body)
#    client_socket.close()
    return str("bpo")


if __name__ == "__main__":
    app.run(debug=True)
