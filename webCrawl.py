import urllib.request
import sys
from bs4 import BeautifulSoup

# Crawls a webpage and returns the number of instances of a given word
 
def main(argv):
    url = "https://en.wikipedia.org/wiki/Oktoberfest"
    if len(sys.argv) == 1:
        print("No word entered in commandline")
        return
    elif len(sys.argv) > 2:
        print("Too many words entered, just one word please")
        return
    else:
        word = argv[1]
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    for script in soup(["script", "style"]): # Get rid of all script and style elements
        script.extract() 
    
    text = soup.get_text() # Get text from webpage
    count = text.count(word)# Get count of requested word
    print('\nUrl: {}\nContains {} occurrence(s) of word: {}'.format(url, count, word))
 
if __name__ == '__main__':
    main(sys.argv)

