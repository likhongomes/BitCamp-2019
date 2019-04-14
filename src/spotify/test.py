# 1/usr/bin

import spotipy
sp = spotipy.Spotify()

results = sp.search(q='Beyonce', limit=20)

for i, t in enumerate(results['tracks']['items']):
    print(i, t['name'])
