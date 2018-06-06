import urllib.request
import sys
from bs4 import BeautifulSoup

# Crawls a webpage and returns the number of instances of a given word

def main():
	while True:
		try:
			url = input("Enter a URL (exactly as-is in url bar) or type 'q' to quit: ")
			if url == 'q':
				print("Goodbye!")
				return False	
			word = input("Enter word to crawl site for: ")
			html = urllib.request.urlopen(url).read()
			soup = BeautifulSoup(html, "lxml")
			for script in soup(["script", "style"]): # Get rid of all script and style elements
				script.extract() 		
			text = soup.get_text() # Get text from webpage
			count = text.count(word)# Get count of requested word
			print('\nUrl: {}\nContains {} occurrence(s) of word: {}'.format(url, count, word))
			print("\n")
		except ValueError:
			print("\nInvalid URL, please try again\n")
 
if __name__ == '__main__':
    main()

