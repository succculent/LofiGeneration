import requests
from lxml import html

page = requests.get('https://www.sltrib.com/news/education/2020/03/04/after-byu-honor-code/')
contents = page.content
tree = html.fromstring(contents)
articleText = tree.xpath('//div[@id="article-body"][@class="article-body article-body-elements"]/text()')
print(articleText)
