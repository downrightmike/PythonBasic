import urllib.request

page = urllib.request.urlopen("http://127.0.0.1:63517/index.html")
text = page.read().decode("utf8")
price = text[234:238]


print(price)
