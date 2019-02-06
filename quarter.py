import xlrd 
import nltk
import re
import json
from nltk.tokenize import word_tokenize
from openpyxl import load_workbook
 
# Creat a dictionary for data storage
all_drug = {}

# Create a corpus of stopwords
stopwords = ['','plus','alone','vaccine','matching','with','placebo','to','of','pills',
				'drug','biological','injection','therapy', 'dose','tablet','administered',
				'as','either','two','one','treatment','implantation','control','active','comparator',
				'local','infusion','drug','levels','challenge','in','upper','arm','muscle',
				'sugar','pill','background','and','group','therapy','mg','treatment','days','following',
				'test','product','reference','ca','irvine','stem','cells','matching','low',
				'range','the','inc','cell','for','a','b','injection','protocol','placebos','oral'
				'fix','fixed','side','effect','level','taken','every','minutes','or','ml']

def check_empty(s):
	return bool(s and s.strip())


# Get content with label, without |
# Input: string
# Output: dictionary of content 

def get_content(sentence):
	# get rid of |
	item = {}
	if check_empty(sentence) == True:

		if "|" in sentence:
			sentence = re.split('\|', sentence) # now sentence is a list
			title = word_tokenize(sentence[0])[0]
			item[title] = []
			for element in sentence:
				element = re.split('\:', element)
				item[title].append("".join(element[1:]))
			print(item)		
		if "|" not in sentence:
			title = word_tokenize(sentence)[0]

			item[title] = []
			sentence = re.split('\:', sentence)
			item[title].append("".join(sentence[1:]))
	else:
		item["NO Data"] = "No data entered"
	
	return item

def get_icd(sentence):
	number = []
	if "|" in sentence:
		sentence = re.split('\|', sentence)
		for num in sentence:
			number.append(num)
	else:
		number.append(sentence)

	return number
# Read file into python with NCT Number, ICD 10, Interventions
# Input: excel file name
# Output: excel object 

def open_excel(name):

	disease_open = xlrd.open_workbook(name)
	disease_sheet = disease_open.sheet_by_index(0)
	row = disease_sheet.nrows
	for i in range(1, row):
		NCT = disease_sheet.cell_value(i,2)
		content  = disease_sheet.cell_value(i,8)
		ICD = disease_sheet.cell_value(i,28)
		ICD_list = get_icd(ICD)
		content_dic = get_content(content)
		all_drug[NCT] = {"ICD": ICD_list}
		all_drug[NCT].update(content_dic)

	print(all_drug)
	with open('q1.json', 'w') as fp:
	    json.dump(all_drug, fp)

	return all_drug

# Get data and store them into dictionary, dump dictionary into json file
# Input: excel object
# Output: JSON file
"""
def get_data(sheet,row):

	# Process elements in each row
	for i in range(1,row): 
		currDrug = sheet.cell_value(i,9)   # Interventions
		NCT = sheet.cell_value(i,2)   # NCT number
		druglist = re.split('\|',currDrug)
		all_drug[NCT] = druglist
		# Find out the only two types of data we want in this row
		for value in all_drug[NCT]:
			if "Drug" in word_tokenize(value) :
				for i in range(0,len(value)):
					if value[i] == ":":
						all_drug[NCT] = {"Drug": value[i+1:]}
			elif 'Biological' in word_tokenize(value):
				for i in range(0,len(value)):
					if value[i] == ":":
						all_drug[NCT] = {"Biological": value[i+1:]}
			else:
				all_drug.pop(NCT, None)
	
	for i in range(1,7465):
		for nct_number in word_tokenize(disease_sheet.cell_value(i, 2)):
			disease_kind = {"disease":[disease_sheet.cell_value(i, 7),disease_sheet.cell_value(i, 29)]}
			unknown = {"disease": "Do not know yet"}
			dict(all_drug[nct_number].items() + disease_kind.items())

	with open('q1.json', 'w') as fp:
	    json.dump(all_drug, fp)

	return all_drug
	
"""
if __name__ == "__main__":

	name = ("trials_classified2018.xlsx")
	print(open_excel(name))
	#get_data(disease_sheet,row)


# druglist = [d for d in druglist if 'Drug' in d or 'Biological' in d]
# currDrug = ' '.join(druglist)
# druglist = re.split('\s|\/|\,|\(|\)|\%|',currDrug)

# druglist = [d for d in druglist if d.lower() not in stopwords]
#print(''.join(druglist))
#for line in ''.join(druglist):


