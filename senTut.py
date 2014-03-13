import sqlite3
import time


conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

negativeWords = []
positiveWords = []

sql = "SELECT * FROM wordVals WHERE value =?"


def loadWordArrays():
    for negRow in c.execute(sql, [(-1)]):
        negativeWords.append(negRow[0])
    print 'neg words loaded'

    for posRow in c.execute(sql, [(1)]):
        positiveWords.append(posRow[0])

    print 'pos words loaded'

def testSentiment():
    readFile = open('positiveIMDB.txt','r').read()

    sentCounter = 0

    for eachPosWord in positiveWords:
        if eachPosWord in readFile:
            sentCounter += 1
    for eachNegWord in negativeWords:
        if eachNegWord in readFile:
            sentCounter -= 1

    if sentCounter > 0:
        print 'this text is pos'

    if sentCounter == 0:
        print 'this text is neut'

    if sentCounter < 0:
        print 'this text is neg'

    print sentCounter

loadWordArrays()
testSentiment()
