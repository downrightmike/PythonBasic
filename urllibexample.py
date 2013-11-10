import urllib.request

page = urllib.request.urlopen('http://amazon.com/index.html')
text = page.read().decode("utf8")

print(text)
