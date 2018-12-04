
import xml.dom.minidom

DOM = xml.dom.minidom
doc = DOM.parse(open("example.xml"))
x = doc.getElementsByTagName("hint")[0]
x.tagName = "note"
print(x.toxml("utf-8"))