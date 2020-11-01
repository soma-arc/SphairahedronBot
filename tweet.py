import tweepy

consumer_key = 'xxx'
consumer_secret = 'xxx'

access_token = 'xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#api.update_status('test tweet');
#api.update_with_media(status = 'test tweet with media', filename = 'flame.png')

filenames = ['flame.png', 'loxoExponential.png',
             'fractalFlame.png', 'kleinianWalker.png']
media_ids = []
for filename in filenames:
        res = api.media_upload(filename)
        media_ids.append(res.media_id)

api.update_status(status='four images!', media_ids=media_ids)
