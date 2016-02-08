import requests
import sys
from lxml import html
import re
from bs4 import BeautifulSoup
import csv
i = 1
cw = csv.writer(open("amazon.csv",'w'))
seller_id = "A14UQ4H17XUX90"
while(True):
	print i
	url="http://www.amazon.in/gp/aag/ajax/paginatedFeedback.html?seller="+seller_id+"&currentPage="+str(i)
	
	response = requests.get(url)
	web_content = response.content
	soup = BeautifulSoup(web_content)

	all_data = soup.find_all('li',{'class' : 'feedbackRow feedbackRow-even'})

	all_data = all_data + soup.find_all('li',{'class' : 'feedbackRow feedbackRow-odd'})
	
	if(len(all_data) == 0):
		break

	for row in all_data:
		row_in = row.find('ul')
		baz = []
		for foo in row_in.find_all('li'):
			baz.append(foo.contents[0])
		try:
			cw.writerow(list(baz))
		except UnicodeEncodeError:
			pass

	i = i + 1