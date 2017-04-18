from bs4 import BeautifulSoup
import urllib
import urllib.request
import sys
import io
import re
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

page_num=15
#index_url='http://search.cnki.com.cn/Search.aspx?q=%E6%A0%91&rank=relevant&cluster=Type&val=D049&p='  #+str(page_num)


def get_paper_url(page_url):
    html = urllib.request.urlopen(page_url).read()
    soup = BeautifulSoup(html,'html.parser')
    #print(soup.find_all('div', class_='wz_content',a))
    #pp=soup.findAll('a',attrs={'href':re.compile('^http'),'id':'link1'})
    p1 = soup.findAll(attrs={'href':re.compile('^http://www.cnki.com.cn/'),'target':'_blank'})
    p2 = soup.findAll(attrs={'href':re.compile('^http://cdmd.cnki.com.cn/'),'target':'_blank'})
    p3 = soup.findAll(attrs={'href':re.compile('^http://cpfd.cnki.com.cn/'),'target':'_blank'})
    f = open('data.txt','a+')
    for url in p1:
        #print(url.get('href'))
        f.write(url.get('href')+'\n')
    for url in p2:
        f.write(url.get('href')+'\n')
    for url in p3:
        f.write(url.get('href')+'\n')
    f.close()

if __name__ == '__main__':
    start = time.clock()
    index_url='http://search.cnki.com.cn/Search.aspx?q=%E6%A0%91&rank=relevant&cluster=Type&val=D049&p='
    for i in range(0,68):
        page_num=15
        page_str_num=i*page_num
        page_url=index_url+str(page_str_num)
        #get_page_url(i)
        get_paper_url(page_url)
    end = time.clock()
    print ('Running time: %s Seconds'%(end-start))