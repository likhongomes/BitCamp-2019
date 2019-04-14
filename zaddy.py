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
    text = ""
    # Start our response
    resp = MessagingResponse()
    message = client.messages.list()
    song_input = message[0].body
    print(song_input)
    song_list = search_song(song_input)
    text = "-Response- -\n"
    for song in song_list:
        #print(song)   #list to string
        # Add a message
        text += song +'\n'

    resp.message(text)

    return str(resp)

def search_song(song_input):
    #song_input = message[0].body
    #def search(self, q, limit=10, offset=0, type='track', market=None):
    """ searches for an item
            Parameters:
                - q - the search query
                - limit  - the number of items to return
                - offset - the index of the first item to return
                - type - the type of item to return. One of 'artist', 'album',
                         'track' or 'playlist'
                - market - An ISO 3166-1 alpha-2 country code or the string from_token.
        """
    #results = Spotify.search(self, song_input, limit=5, type='track')

    import spotipy
    from spotipy import util
    from spotipy.oauth2 import SpotifyClientCredentials
    
    song_list = []

    client_credentials_manager = SpotifyClientCredentials(
        client_id="d1e6626ccc62404b98c29295a998a578", client_secret="8d48393fd316432db8b2a40c99662c25")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q=song_input, limit=5)
    counter = 0
    song_list=[]
    for k, v in results.items():
        for i in v['items']:
            song_list.append(i['name'])
            counter = counter + 1
        counter = 0

    return song_list
    

if __name__ == "__main__":
    app.run(debug=True)
