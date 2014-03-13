from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'vgxbOmSgetrNEa1l1AmTpw'
csecret = 'iiTOwa7MUAuVyek2zb8fYqCQ9EeZwHXew6NjaC7VY'
atoken = '363671726-XuePgVt94MWQGc94LhnYwT6deLESs4FDwxK69Fci'
asecret = '6HyZQ6BQk0LuCKSG6k03FDjILPrvSORxOQgqb2G9BwY'

class listener(StreamListener):

    def on_data(self, data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]
            #print tweet
            saveThis = str(time.time())+'::'+tweet
            saveFile = open('twitDB.csv', 'a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata, ',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
