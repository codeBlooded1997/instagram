import requests
from bs4 import BeautifulSoup


class InstaScraper:
	results = []

	def fetch(self, url):
		return requests.get(url)

	def parse(self, html):
		content = BeautifulSoup(html, 'html.parser')

		tag = content.find('meta', {'name': 'description'})
		text = tag.attrs['content']
		main_text = text.split(",")
		#main_list = main_text.split(',')
		for each in main_text:
			self.results.append(each)
		print(self.results)
		print(type(self.results))
		print(len(self.results))

	def run(self):
		#url = 'https://www.instagram.com/{}/'.format(user_id)
		response = self.fetch("https://www.instagram.com/9gag/")
		self.parse(response.content)

if __name__ == '__main__':
    scraper = InstaScraper()
    scraper.run()


#URL = "https://www.instagram.com/{}/"

#def scrape(username):
#	full_url = URL.format(username)
#	response = requests.get(full_url)
#	soup = BeautifulSoup(response.content, 'html.parser')

#	tag = soup.find('meta', {'name':'description'})
#	text = tag.attrs['content']
#	main_text = text.split("_")[0]

#	return main_text

#USERNAME  = '9gag'
#data = scrape(USERNAME)
#print(data)

