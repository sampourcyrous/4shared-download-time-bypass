import codecs
import re
import urllib.request

class downloadMP3:

    def __init__(self, filename):
        self.filename = filename
        self.fileArray = self.fileToArray()
        self.fileString = self.fileToString()
        self.pageLinks = self.getPageLinks()
        self.realLinks = self.getRealLinks()
        self.downloadLinks = self.getDownloadLinks()
        self.downloadSongs()
    
    '''Add file contents to array'''
    def fileToArray(self):
        self.fileArray = []
        file = codecs.open(self.filename, "r", "utf-8")
        array = []
        for line in file:
            array.append(line)
        file.close()
        
        return array
    
    '''Add file contents to string'''
    def fileToString(self):
        self.fileString = ""
        file = codecs.open(self.filename, "r", "utf-8")
        string = ""
        for line in file:
            string += line
        file.close()
        
        return string

    '''Get page links listed in source code using regular expressions'''
    def getPageLinks(self):
        prevIndex = 0
        searchString = "href"
        links = []

        numOfLinks = self.fileString.count("href")
        
        while (numOfLinks > 0):
            nextIndex = self.fileString.index(searchString, prevIndex+1)
            m = re.search('(\".+?\")', self.fileString[nextIndex:])
            links.append(m.group(0).strip('"'))
            prevIndex = nextIndex
            numOfLinks -= 1
        return links
    
    def getRealLinks(self):
        realLinks = []
        
        for links in self.pageLinks:
            if links.count("shared") > 0:
                realLinks.append(links)
                
        return realLinks
    
    def getDownloadLinks(self):
        downloadLinks = []
        searchString = "file:"

        for links in self.realLinks:
            url = urllib.request.urlopen(links).read()
            m = re.search('(file: ".+?")', str(url))
            if m != None:
                cleanUrl = m.group(0)[m.group(0).index("http"):]
                cleanUrl = cleanUrl[:-1]
                downloadLinks.append(cleanUrl)
            
        return downloadLinks
    
    def downloadSongs(self):
        count = 1
        
        for links in self.downloadLinks:
            songName = "mp3Songs/song" + str(count) + ".mp3"
            urllib.request.urlretrieve(links, songName)
            count += 1
    
mp3 = downloadMP3("mp3.html")
print("Finished!")