
import feedparser
import re


def getwords(html):
    txt = re.compile(r'<[^>]+>').sub('', html)
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower() for word in words if word != '']


def getwordcounts(url):
    
    urlContent = feedparser.parse(url)
    wordCount = {}

    if 'title' not in urlContent.feed:
        return "NULL"

    for entry in urlContent.entries:
        if 'summary' in entry:
            summary = entry.summary
        else:
            summary = entry.description

        words = getwords(entry.title + ' ' + summary)
        for word in words:
            wordCount.setdefault(word, 0)
            wordCount[word] += 1
        
    return urlContent.feed.title, wordCount


apcount = {}
wordcounts = {}
feedlist = [line for line in file('feedlist.txt')]

for feedurl in feedlist:
    title, wc = getwordcounts(feedurl)
    wordcounts[title] = wc
    for word, count in wc.items():
        apcount.setdefault(word, 0)
        if count > 1:
            apcount[word] += 1


wordlist = []
for w, bc in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5: wordlist.append(w)

out = file('blogdata.txt', 'w')
out.write('Blog')
for word in wordlist: out.write("\t%s" % word)
out.write('\n')
for blog, wc in wordcounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wc : out.write("\t%s" % wc[word])
    else:
        out.write("\t0")
out.write('\n')
    

    
