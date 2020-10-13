# pip install --upgrade lxml

import xml.etree.ElementTree as ET
tree = ET.parse('example.xml')  #file you wanna parse
root = tree.getroot()

##### simiple example of print function of relativce path in xml ######
# print(root.findall('.//module'))     

##### simiple example of printing for-loop of rel & absolute path ######
# for i in root.findall(".//STUDENT/MARK"):    #relative path. working
# for i in root.findall(".//MARK"):    #relative path. working
# for i in root.findall("./ASSESSMENTS/STUDENT/MARK"):    #absolute path. but it doesnt work ATM
    # print(i)

##### a better approach #####
for student in root.findall('STUDENT'):
    name = student.get('name')
    mark = student.find('MARK').text
    print(name, mark)