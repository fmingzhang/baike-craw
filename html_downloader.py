# coding:utf-8
import requests
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
        rp=requests.get(url,headers=headers)
        if rp.status_code!=200:
            return None
        return rp.content