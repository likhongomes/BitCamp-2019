import spotipy
spotify = spotipy.Spotify()
name = "Ed Sheeran"
results = spotify.search(q='artist:' + name, type='artist')
print results