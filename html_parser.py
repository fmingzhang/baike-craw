# coding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):
    def parse(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont, 'lxml',from_encoding='utf-8')#注明html的编码方式
        new_urls=self._get_new_urls(new_url,soup)
        new_data=self._get_new_data(new_url,soup)

        #print new_urls

        return new_urls,new_data
   #<a target="_blank" href="/item/%E8%83%B6%E6%B0%B4%E8%AF%AD%E8%A8%80/3564482" data-lemmaid="3564482">胶水语言</a>
    def _get_new_urls(self, new_url, soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'^/item/.+'))
        u='https://baike.baidu.com'
        for link in links:
            url=link.get('href')

            full_url=urlparse.urljoin(u,url)

            new_urls.add(full_url)



        return new_urls



    def _get_new_data(self, new_url, soup):
        res_data={}
        res_data['url']=new_url

        title_node=soup.find('div',id="J-vars")
        res_data['title']=title_node.get('data-lemmatitle')
        summary_node=soup.find('ul',id="J-card-sound")
        res_data['summary']=summary_node
        return res_data

