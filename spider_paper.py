# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
#import urllib2
import requests
import time

if __name__ == "__main__":
	start = time.clock()
	#f=urllib2.urlopen(url, timeout=5).read()
	#soup=BeautifulSoup(html)
	#tags=soup.find_all('a')
	file = open("data.txt")
	lines = file.readlines()
	txt_num=1
	for line in lines:
		paper_url = line
		temp = paper_url.split('/')
		file_name = "./data/" + temp[len(temp)-1] + '.txt'
		html = urllib.request.urlopen(paper_url).read()
		soup = BeautifulSoup(html,'html.parser')
		file_content = open(file_name,'a')

		file_content.write("Title:")
		paper_title = soup.find_all('h1',class_="xx_title")
		for thing in paper_title:
			a = thing.strings
			for string in a:
				file_content.write(string)

		file_content.write("\nAuthors:")
		paper_authors = soup.find_all('div',style="text-align:center; width:740px; height:30px;")
		for paper_author in paper_authors:
			names = paper_author.find_all('a',target='_blank')
			for name in names:
				a = name.strings
				for string in a:
					file_content.write(string + ' ')
		
		file_content.write("\nAbstracts:")
		pp=soup.find_all('div',style="text-align:left;word-break:break-all")
		for thing in pp:
			a = thing.strings
			for string in a:
				file_content.write(string)
			txt_num+=1
		file_content.close()
		#[p.next_sibling.strip() for p in soup.find_all('p')]
	file.close()
	end = time.clock()
	print ('Running time: %s Seconds'%(end-start))