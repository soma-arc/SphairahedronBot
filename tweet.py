import argparse
import tweepy

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--images', nargs='*')
parser.add_argument('-d', '--description')

args = parser.parse_args()

print(args.images)

consumer_key = 'xxx'
consumer_secret = 'xxx'

access_token = 'xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

media_ids = []
for filename in args.images:
        print('upload '+ filename)
        res = api.media_upload(filename)
        media_ids.append(res.media_id)

api.update_status(status=args.description,
                  media_ids=media_ids)
print('Tweeted')
