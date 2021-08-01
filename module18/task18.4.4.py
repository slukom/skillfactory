# Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:
# <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>

import requests
import lxml.html
from lxml import etree

html = '<html> <head> <title> Some title </title> </head> <body>  <tag1> some text     <tag2> MY TEXT </tag2>   </tag1> </body></html>'

tree = lxml.html.document_fromstring(html)
tag2 = tree.xpath('body/tag1/tag2/text()')

print(tag2)