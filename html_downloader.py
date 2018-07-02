# coding:utf-8
import requests
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        headers = {}
        rp=requests.get(url,headers=headers)
        if rp.status_code!=200:
            return None
        return rp.content
