# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from spot import add_to_playlist
from spot import list_playlists
from spot import change_playlists
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
account_sid = 'ACf797a6b1926d1b042838e6823133f2ab'
auth_token = 'bd035778a88f156ed5a40acefb612c3a'

client = Client(account_sid, auth_token)
playlist_name = ""
counter = 0
valid_bit = 0
create_bool = False
d = {}


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    global playlist_name
    global counter
    global d
    global create_bool
    """Respond to incoming messages with a friendly SMS."""
    global valid_bit
    text = ""
    # Start our response
    resp = MessagingResponse()
    message = client.messages.list()
    song_input = message[0].body

    song_input = song_input.lower()

    if song_input == 'change playlist':
        text = "-Changing to a Playlist- -\n\nPlease Enter Playlist Name"
        valid_bit = 1
        resp.message(text)
        return str(resp)

    if song_input in list_playlists() and valid_bit == 1:
        change_playlists(song_input)
        print("Successfully changed to ", song_input)
        valid_bit = 0
        text = "Successfully changed to " + song_input
        resp.message(text)
        return str(resp)

    if song_input == "ls playlist":
        string = ""
        playlists = list_playlists()
        for i in playlists:
            string += "" + i + "\n"
        resp.message(string)
        print(playlists)
        return str(resp)

    if song_input == "new playlist":
        counter = 1
        text = "-Creating New Playlist- -\n\nPlease Enter Playlist Name"
        resp.message(text)
        create_bool = True
        return str(resp)

    # when user wants to make a new playlist
    if counter == 1:
        playlist_name = song_input.lower()
        text = "Naming Playlist: " + playlist_name
        text += "\n\nPlease Enter Song"
        resp.message(text)
        counter = 3
        return str(resp)

    if song_input == "faq":
        text = "To create a new playlist, type in \'New Playlist\' \n To put in a new song, type in the song name (and if applicable the artist too!) \n Choose which song you want to get queued! "
        resp.message(text)
        return str(resp)
    if song_input.isdigit() is not True:
        print(song_input)
        song_list, song_ids, artist_list = search_song(song_input)
        for i in range(len(song_list)):
            d[i] = [str(song_ids[i])]

            text = "-Response- -\n"
            temp = 0
        for song in range(len(song_list)):
                # Add a message
            text += str(temp) + ". " + song_list[song] + ' (' + artist_list[song] + ')' + '\n'
            temp += 1
        text += "Choose the number!"
        resp.message(text)
        return str(resp)
    else:
        add_to_playlist(track_id=d[int(song_input)],
                        create_bool=create_bool, playlist_name=playlist_name)
        print("Added the song", d[int(song_input)])
        text = "Added the song " + str(song_input)
        create_bool = False
        resp.message(text)
        return str(resp)
    return str(resp)


def search_song(song_input):
    #song_input = message[0].body
    # def search(self, q, limit=10, offset=0, type='track', market=None):
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

    song_list = []

    client_credentials_manager = SpotifyClientCredentials(
        client_id="d1e6626ccc62404b98c29295a998a578", client_secret="8d48393fd316432db8b2a40c99662c25")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q=song_input, limit=10)
    counters = 0
    song_list = []
    artist_list = []
    song_ids = []
    for k, v in results.items():
        for i in v['items']:
            song_list.append(i['name'])
            song_ids.append(i['id'])
            artist_list.append(i['artists'][0]['name'])
            counters = counters + 1
        counters = 0

    return song_list, song_ids, artist_list


if __name__ == "__main__":
    app.run(debug=True)
