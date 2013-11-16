import urllib
import time

username = "UserName"
password = "Password!"

def send_to_twitter(msg):
	password_manager = urllib.HTTPPasswordMgr()
	password_manager.add_password("Twitter API", "http://twitter.com/statuses", username, password)
    http_handler = urllib.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.build_opener(http_handler)	
    urllib.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg})
    resp = urllib.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()	
    
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
    send_to_twitter(get_price())
else:
    price = 99.99

    while price > 4.74:
        time.sleep(900)
        price = get_price()
    send_to_twitter("Buy!")
