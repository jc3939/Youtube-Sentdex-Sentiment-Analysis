import sqlite3
import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time
import nltk
import datetime

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5,0')]

conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

def createDB():
    c.execute("CREATE TABLE wordVals (word TEXT, value REAL)")
    
startingWord = 'good'
startingWordVal = 1

synArray = []

def main():
    try:
        page = 'http://thesaurus.com/browse/' + startingWord+ '?s=t'
        sourceCode = opener.open(page).read()

        try:
            #print sourceCode
            synoNym = sourceCode.split('<td valign="top">Synonyms:</td>')
            x = 1
            while x<len(synoNym):
                try:
                    synoNymSplit = synoNym[x].split('</span></td>')[0]
                    synoNyms = re.findall(r'\">(\w*?)</a>', synoNymSplit)
                    print synoNyms
                    for eachSyn in synoNyms:
                        query = "SELECT * FROM wordVals WHERE word =?"
                        c.execute(query, [(eachSyn)])
                        data = c.fetchone()

                        if data is None:
                            print 'not here yet, let us add it'
                            c.execute('INSERT INTO wordVals (word, value) VALUES (?, ?)',
                                      (eachSyn, startingWordVal))
                            conn.commit()
                        else:
                            print 'word already here!'
                        
                except Exception, e:
                    print str(e)
                    print 'failed in 3rd try'

        except Exception, e:
            print str(e)
            print 'failed 2nd try'

    except Exception, e:
        print str(e)
        print 'failed main loop'

main()

c.execute("INSERT INTO doneSyns (word, value) VALUES (?)",
          (startingWord))

conn.commit()
