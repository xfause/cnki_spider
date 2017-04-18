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
	txt_num=1;
	for line in lines:
		file_name='./data/out_'+str(txt_num)+'.txt'
		paper_url = line
		html = urllib.request.urlopen(paper_url).read()
		soup = BeautifulSoup(html,'html.parser')
		pp=soup.find_all('div',style="text-align:left;word-break:break-all")
		fuck = open(file_name,'a')
		for thing in pp:
			a = thing.strings
			for string in a:
				fuck.write(string)
			txt_num+=1
		fuck.close()
		#[p.next_sibling.strip() for p in soup.find_all('p')]
	file.close()
	end = time.clock()
	print ('Running time: %s Seconds'%(end-start))