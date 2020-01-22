import requests
from bs4 import BeautifulSoup

URL = "https://www.instagram.com/{}/"

def scrape(username):
	full_url = URL.format(username)
	response = requests.get(full_url)
	soup = BeautifulSoup(response.content, 'html.parser')

	tag = soup.find('meta', {'name':'description'})
	text = tag.attrs['content']
	main_text = text.split("_")[0]

	return main_text

USERNAME  = '9gag'
data = scrape(USERNAME)
print(data)
