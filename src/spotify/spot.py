# 1/usr/bin/python
import spotipy
from spotipy import util

username = "128501948"
playlist = "spotify:user:128501948:playlist:2xiBCO9WzBlYqE70z9MaUo"


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
                                    track['name']))


# void variable that only changes the global variable playlists
def change_playlists(playlist_name):
    global playlist
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(
        username, scope, client_id="d1e6626ccc62404b98c29295a998a578", client_secret="8d48393fd316432db8b2a40c99662c25", redirect_uri="https://open.spotify.com/playlist/5yBW13vPeKHCYENcMvOirv")

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlis in playlists['items']:
            if playlis['owner']['id'] == username:
                if playlis['name'].lower() == playlist_name.lower():
                    playlist = playlis['uri']
                    print("YES")
    else:
        print("Can't get token for", username)


def list_playlists():
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(
        username, scope, client_id="d1e6626ccc62404b98c29295a998a578", client_secret="8d48393fd316432db8b2a40c99662c25", redirect_uri="https://open.spotify.com/playlist/5yBW13vPeKHCYENcMvOirv")

    temp = []
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlis in playlists['items']:
            if playlis['owner']['id'] == username:
                temp.append(playlis['name'].lower())
    else:
        print("Can't get token for", username)

    return temp


def add_to_playlist(track_id, playlist_name="", create_bool=False):
    global playlist
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(
        username, scope, client_id="d1e6626ccc62404b98c29295a998a578", client_secret="8d48393fd316432db8b2a40c99662c25", redirect_uri="https://open.spotify.com/playlist/5yBW13vPeKHCYENcMvOirv")

    # test playlist id [tommy's hardcoded]

    # test adding track to playlist
    #track_id = ["5CXmbqFE0mRXOYXgEze8q3"]

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        # creates a playlist
        if create_bool is True:
            plist = sp.user_playlist_create(user=username, name=playlist_name)
            plist = playlist['id']
            results = sp.user_playlist_add_tracks(username, plist, track_id)

        #results = sp.current_user_playlists()
        # adds track to playlist ONLY if it create playlist isn't provided
        else:
            results = sp.user_playlist_add_tracks(username, playlist, track_id)

        ''' reads from playlist '''
        # this gets the playlist URI
        #playlist = sp.user_playlist(username, playlist, fields="tracks,next")

    else:
        print("Can't get token for", username)


# add_to_playlist(track_id=["5CXmbqFE0mRXOYXgEze8q3"], create_bool=True, playlist_name="bruh")
