import urllib
import time

def get_price():
	price = urllib.urlopen("http://")
	text = page.read().decode("utf8")
	where = text.find('>$')
	start_of_price = text + 2
	end_of_price = start_of_price +4
	return(text[start_of_price:end_of_price])
get_price()

price_now = input("Do you need a price right now? (Y/N)")
if price_now == "Y":
    print(get_price)
else:
    price = 99.99

    while price > 4.74:
        time.sleep(900)
        price = get_price()
    print ("Buy!")
