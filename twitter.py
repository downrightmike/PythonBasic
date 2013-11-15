def send_to_twitter():
	msg = "I am a msg!"
	password_manager = urllib.HTTPPasswordMgr()
	password_manager.add_password("Twitter API",
										"http://twitter.com/statuses", "username", "password")
http_handler = urllib.HTTPBasicAuthHandler(password_manager)
page_opener = urllib.build_opener(http_handler)	
urllib.install_opener(page_opener)
params = urllib.parse.urlencode( {'status': msg})
resp = urllib.urlopen("http://twitter.com/statuses/update.json", params)
resp.read()									