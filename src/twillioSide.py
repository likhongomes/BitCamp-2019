import pyrebase

def push_to_db(url):
    config = {
        "apiKey": "AIzaSyDp11PzE0mcTxyerGJzz0BYBFTxhCQIN_g",
        "authDomain": "projectId.firebaseapp.com",
        "databaseURL": "https://tcnj-music-player.firebaseio.com/",
        "storageBucket": "tcnj-music-player.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    db.child("Playlist").child()
    data = {"Song": url}
    db.push(data)
    print("Finished uploading to firebase")
