from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf797a6b1926d1b042838e6823133f2ab"
# Your Auth Token from twilio.com/console
auth_token  = "bd035778a88f156ed5a40acefb612c3a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12673919040", 
    from_="12672742451",
    body="Hello from Python!")

print(message.sid)
