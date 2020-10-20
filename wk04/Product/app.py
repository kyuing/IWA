# from IPython.core.display import display, HTML
# display(HTML('product.xml'))
from bs4 import BeautifulSoup
from io import StringIO
import lxml.etree as ET
from IPython.core.display import display, HTML

dom = ET.parse('product.xml')
xslt = ET.parse('product.xsl')
transform = ET.XSLT(xslt)
newdom = transform(dom)
result = BeautifulSoup(ET.tostring(newdom, pretty_print=True))


display(HTML(result.prettify()))