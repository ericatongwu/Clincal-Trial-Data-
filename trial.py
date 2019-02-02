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

# Read file into python with NCT Number, ICD 10, Interventions
# Input: excel file name
# Output: excel object 

def open_excel(name):

	disease_open = xlrd.open_workbook(name)
	disease_sheet = disease_open.sheet_by_index(0)
	print(disease_sheet.nrows)
	return disease_sheet

# Get data and store them into dictionary, dump dictionary into json file
# Input: excel object
# Output: JSON file
"""
def get_data(sheet):

	# Process elements in each row
	for i in range(1,len(sheet)): 
		currDrug = sheet.cell_value(i,7)
		NCT = sheet.cell_value(i,1)
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
			disease_kind = {"disease":[disease_sheet.cell_value(i, 7),disease_sheet.cell_value(i, 28)]}
			unknown = {"disease": "Do not know yet"}
			dict(all_drug[nct_number].items() + disease_kind.items())

	with open('result.json', 'w') as fp:
	    json.dump(all_drug, fp)

	return all_drug
	

print(get_data(sheet, disease_sheet))
"""
if __name__ == "__main__":

	name = ("trials_classified2018.xlsx")
	open_excel(name)
	# sheet = open_excel(name)
	#get_data(sheet)


# druglist = [d for d in druglist if 'Drug' in d or 'Biological' in d]
# currDrug = ' '.join(druglist)
# druglist = re.split('\s|\/|\,|\(|\)|\%|',currDrug)

# druglist = [d for d in druglist if d.lower() not in stopwords]
#print(''.join(druglist))
#for line in ''.join(druglist):


