import urllib.request

page = urllib.request.urlopen("http://127.0.0.1:63517/index.html")
text = page.read().decode("utf8")

where = text.find('>?')

start_of_price = where + 2
end_of_price = start_of_price + 4

price = text[start_of_price:end_of_price]


print(price)
