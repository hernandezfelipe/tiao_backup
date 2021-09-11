import tweepy
from datetime import datetime

def post_picture(image_path, msg=None):

    # personal details
    consumer_key ="OX7LYeIO08Ac6GIcXKWNw2l9B"
    consumer_secret ="sD4bLfwJqZ7MDvx19J2h9UjZJHNQFXvku2oUZMeFk6Vo0k0DnG"
    access_token ="878744744767172608-d04q5pSyaLHnWlICqueyg2W9nZJg1k8"
    access_token_secret ="IJMV9hZTFIlrEJ5q7ov2jVJ2thReFY849jx3DC8tUXjFj"

    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    now = datetime.now()
    time_id = '{:02d}'.format(now.hour)+":"+'{:02d}'.format(now.minute)+":"+'{:02d}'.format(now.second)

    if msg is not None:
            tweet = msg
    else:
            tweet = "Olar ("+ time_id +")" # toDo
    #image_path ="path of the image" # toDo

    # update the status
    status = api.update_with_media(image_path, tweet)
    api.update_status(status)


if __name__ == "__main__":
    
    post_picture('/home/pi/Desktop/dog_monit/auto_tweet.png',  'Teste')
