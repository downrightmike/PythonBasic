import urllib
import time

price = 99.99

while price > 4.74:
    time.sleep(900)
    page = urllib.request.REQUEST("http://127.0.0.1:63517/index.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = get_price()
print ("Buy!")
