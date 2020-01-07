from urllib.request import urlopen
from bs4 import BeautifulSoup


webpage = 'https://www.coinbase.com/price/bitcoin'

page = urlopen(webpage)			# loads a webpage into a python object


soup = BeautifulSoup(page, 'html.parser')		#using beautifulsoup to parse the html page

title = soup.title

print(title.text)


span = soup.findAll("span")  # find ALL tags 'span'
##print(headers)
price = span[6].text			#price
up_down = span[7].text	   	#+ve or -ve gain 
how_much = span[8].text	   	# by how much

if up_down == '-':
	up_down = 'down'
else:
	up_down = 'up'
print("The current price of bitcoin is:",price)
print("It went", up_down,"by",how_much)                                                      
