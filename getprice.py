import urllib 

def get_price():
	price = urllib.request.urlopen("http://")
	text = page.read().decode("utf8")
	where = text.find('>$')
	start_of_price = text + 2
	end_of_price = start_of_price +4
	return(text[start_of_price:end_of_price])
get_price()