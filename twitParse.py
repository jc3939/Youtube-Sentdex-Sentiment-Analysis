import re
import difflib
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5,0')]

keyWord = 'obama'
startingLink = 'https://twitter.com/search/realtime?q='

def main():
    oldTwit = []
    newTwit = []
    howSimAr = [.5, .5, .5, .5, .5]
    while 1 < 2:
        try:
            sourceCode = opener.open('https://twitter.com/search/realtime?q='+keyWord+'&src=hash').read()
            #print sourceCode
            splitSource = re.findall(r'<p class="js-tweet-text tweet-text">(.*?)</p>', sourceCode)
            
            for item in splitSource:
                #print item
                print ''
                print ''
                print ''
                print '______________________'
                aTweet = re.sub(r'<.*?>', '', item)
                print aTweet
                newtwit.append(aTweet)
            comparision = difflib.SequenceMatches(None, newTwit, oldTwit)
            howSim = comparison.ratio()
            print '#################'
            print 'This selection is', howSim, 'similar to the past'
            howSimAr.append(howSim)
            howSimAr.remove(howSimAr[0])

            waitMultiplier = reduce(lambda x, y:x+y, howSimAr)/len(howSimAr)

            print ''
            print 'The current similarity array:', howSimAr
            print 'Our current Multiplier:', waitMultiplier
            print '###################'
            oldTwit = [None]
            for eachItem in newTwit:
                oldtwit.append(eachItem)
            newTwit = [None]

            time.sleep(howSim*30)
        except Exception, e:
            print str(e)
            print 'errored in the main try'
            time.sleep(555)

main()
