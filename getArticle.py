#coding:utf-8
"""
下载散文，添加到后台
下载地址：
https://www.duanwenxue.com/shige/sanwenshi/
填充地址：
http://127.0.0.1:8000/admin/Article/article/
"""
import requests
from lxml import etree
#散文获取部分

url = "https://www.duanwenxue.com/shige/sanwenshi/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"
}

response = requests.get(url = url,headers = headers)

data = response.content

HTML = etree.HTML(data)
titles = HTML.xpath('//div[@class="list-base-article"]/ul/li/a')
for t in titles:
    href = "https://www.duanwenxue.com"+t.attrib["href"]
article_response = requests.get(url = href,headers = headers)
content = article_response.content
content_html = etree.HTML(content)
title = r'//div[@class="row-article"]/h1'
author = r'//div[@class="face"]/a/span'
cont = r'//div[@class="article-content article-content-sige"]'
content_title = content_html.xpath(title)[0].text
content_author = content_html.xpath(author)[0].text
content_cont = content_html.xpath(cont)

for cont in content_cont:
    print(cont.tag)

