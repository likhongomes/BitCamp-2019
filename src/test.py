from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACf797a6b1926d1b042838e6823133f2ab'
auth_token = 'bd035778a88f156ed5a40acefb612c3a'
client = Client(account_sid, auth_token)
message = client.messages.create(
                              from_='+12672742451',
                              body='body',
                              to='+12673919040'
                          )
amessages = client.messages.list(from_='+12673919040')

print(amessages[0].body)


print()
print(message.sid)
print()
service = client.messaging.services.create(friendly_name='friendly_name')

print(service.links)
