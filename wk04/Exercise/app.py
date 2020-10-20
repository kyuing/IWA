from bs4 import BeautifulSoup
import lxml.etree as ET

dom = ET.parse('WebAppDev.xml')
xslt = ET.parse('WebAppDev.xsl')
transform = ET.XSLT(xslt)
newdom = transform(dom)
result = BeautifulSoup(str(newdom))
print(result.prettify())

# http://xsltransform.net/93Q1PL3/4