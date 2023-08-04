from bs4 import BeautifulSoup
import requests
import time
import schedule


def core():
	global c
	url  = "https://www.oberlo.com/blog/motivational-quotes"
	result = requests.get(url)
	doc = BeautifulSoup(result.text, "html.parser")

	quotes = doc.find_all("li", style="font-weight: 400;")
	quote_list = []
	for i in quotes:
		quote_list.append(i.text) 
	n=3
	del quote_list[len(quote_list) - n:]
	print(c)
	requests.post("https://ntfy.sh/ozonenotifapp",
	data=quote_list[c].encode(encoding='utf-8'))
	c=c+1
c=0
schedule.every(5).seconds.do(core)
while 1:
	schedule.run_pending()
	time.sleep(1)

