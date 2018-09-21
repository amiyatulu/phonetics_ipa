import pickle
from nltk.tokenize import word_tokenize
import nltk
nltk.data.path.append("nltk_data")

import argparse

parser = argparse.ArgumentParser(description="IPA format")
parser.add_argument("-f1","--file1", help="Enter the input file1 path")
parser.add_argument("-o","--out", help="Out Put path")


args = parser.parse_args()

file1 = args.file1
out = args.out

ipa = pickle.load( open( "ipa.p", "rb" ) )

file_data = open(file1,"r")
data = file_data.read()
# print(data)

tokens = word_tokenize(data)
#print(tokens)
ipa_data = []
for tok in tokens:
	ipa_data.append(ipa.get(tok.lower(),"---"))

file2 = open(out+'myipa.html','w')
print("""
	<!doctype html>
<html lang="en">
<head>
<title>IPA</title>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="author" content="">
</head>""", file=file2)
for t, d in zip(tokens, ipa_data):
	print("<b>"+ t + "</b>"+ '<span style="color:blue;">/' + str(d) +'/</span>' + " ", end="",file=file2)

print("""
</html>""", file=file2)
