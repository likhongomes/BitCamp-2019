#!/usr/bin/env python3
import time
from twilio.rest import Client
from youtube import youtube_search
from twilio.twiml.messaging_response import MessagingResponse

# global variable to stop the spamming of API calls
message_id = 0


def search():
    global message_id

    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'ACf797a6b1926d1b042838e6823133f2ab'
    auth_token = 'bd035778a88f156ed5a40acefb612c3a'
    client = Client(account_sid, auth_token)

    while True:
        time.sleep(5)

        amessages = client.messages.list(from_='+12673919040')
        first = amessages[0].sid
        if first == message_id:
            print("same video")
            continue
        else:
            data = amessages[0].body
            test = youtube_search(str(data))  # returns JSON object
            videos = test[1]  # first video
            video_dict = {'videoID': []}
            video_link = []
            for vid in videos:
                video_dict['videoID'].append(vid['id']['videoId'])
                temp = "https://www.youtube.com/watch?v=" + vid['id']['videoId']
                video_link.append(temp)

            print("THIS IS YT SEARCH", video_link[0])
            # Start our response
        # push_to_db(str(video_link[0]))
        message_id = first


if __name__ == "__main__":
    search()
