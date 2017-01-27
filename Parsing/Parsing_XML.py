''''Parse XML File'''
import xmltodict

with open('Data/devoe_moore_center_blog_content.xml') as fd:
    doc = xmltodict.parse(fd.read())
print(doc)

print(doc['item']['title'])
