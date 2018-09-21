import pickle
from lxml import etree


ipa = {}

tree = etree.parse("ipa.xml")
r = tree.xpath('/Workbook/Worksheet/Table/Row')

for row in r:
	data = row.xpath("Cell/Data")
	ipa_2 = []
	for datum in data:
		ipa_2.append(datum.text)
		#print(datum.text)
	ipa[ipa_2[0]] = ipa_2[1]


#print(ipa)
pickle.dump(ipa, open("ipa.p", "wb"))