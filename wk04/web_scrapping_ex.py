# pip install requests
import lxml.html
import requests

url = "https://www.imdb.com/calendar?region=IEref_=rlm"
res = requests.get(url, stream=True)
res.raw.decode_content = True
tree = lxml.html.parse(res.raw)

for i in tree.xpath('//div[@id="main"]/h4[text()="23 October 2020"]/following-sibling::*[1]/li/a/text()'):
# for i in tree.xpath('//div[@id="main"]/h4/following-sibling::*[1]/li/a/text()'):
    print(i)
