

import feedparser
import socket
import re

#set default timer for feedparser.
socket.setdefaulttimeout(5.0)


def getWords(html):
    txt = re.compile(r'<[^>]+>').sub('', html)
    
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    return [word.lower() for word in words if word != '']

def parseUrl(url):
    try:
        parseResult = feedparser.parse(url)
    except:
        print "error to open %s" % url
        return "None", {}

    wordCount = {}

    for entry in parseResult.entries:

        if 'summary' in entry:
            summary = entry.summary
        else:
            summary = entry.description

        words = getWords(entry.title + ' ' + summary)
        for word in words:
            wordCount.setdefault(word, 0)
            wordCount[word] += 1
        
    try:
        title = parseResult.feed.title
    except:
        title = "no title"

    return title, wordCount

def parseRssFile(fileName):
    urlList = [url for url in file(fileName)]
    for url in urlList:
        print "parse url: %s" % url
        (title, wordDic) = parseUrl(url)
        print title



if __name__ == "__main__":
    parseRssFile("feedlist.txt")
