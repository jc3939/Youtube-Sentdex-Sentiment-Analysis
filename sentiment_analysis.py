import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5,0')]

def main():
    try:
        page = 'http://feeds.huffingtonpost.com/huffingtonpost/raw_feed'
        sourceCode = opener.open(page).read()
        #print sourceCode
        try:
            titles = re.findall(r'<title>(.*?)</title>', sourceCode)
            links = re.findall(r'<link.*?href="(.*?)"', sourceCode)
            
            
            #for title in titles:
                #print title
            for link in links:
                if '.rdf' in link:
                    pass
                else:
                    print 'Let\'s visit:',link
                    linkSource = opener.open(link).read()
                    #print linkSource
                    content = re.findall(r'<p>((.|\n)*)<p class="video_box_title">(.*?)</p>',linkSource)
                    lineOfInterest = re.findall(r'<p>(.*?)</p>',str(content))
                    for eachLine in lineOfInterest:
                        print eachLine
                    time.sleep(5)
                    
        except Exception, e:
            print str(e)
    except Exception, e:
        print str(e)

main()
