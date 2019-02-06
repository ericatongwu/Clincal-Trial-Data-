import xlrd 
import nltk
import re
import json
from nltk.tokenize import word_tokenize
from openpyxl import load_workbook



sentence = "Drug: Sof+Ledi+R arm|Drug: Sof+Ledi+R+Peg-IFN arm|Drug: Sof+Dacla+R arm|Drug: Sof+Dacla+R+Peg-IFN arm|Drug: Sof+Velpa+R arm|Drug: Sof+Velpa+R+Peg-IFN arm"
sentence1 = "Other: Questionnaire quality of life"

def get_content(sentence):
	# get rid of |
	item = {}
	if "|" in sentence:
		sentence = re.split('\|', sentence) # now sentence is a list
		title = word_tokenize(sentence[0])[0]
		item[title] = []
		for element in sentence:
			element = re.split('\:', element)
			item[title].append("".join(element[1:]))
			
	else:

		title = word_tokenize(sentence)[0]
		item[title] = []
		sentence = re.split('\:', sentence)
		item[title].append("".join(sentence[1:]))
	
	return item

print(get_content(sentence1))
print(get_content(sentence))