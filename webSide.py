import pyrebase

config = {
    "apiKey": "AIzaSyDp11PzE0mcTxyerGJzz0BYBFTxhCQIN_g",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://tcnj-music-player.firebaseio.com/",
    "storageBucket": "tcnj-music-player.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

users = db.child("Playlist").shallow().get()
print(users.val
()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}
