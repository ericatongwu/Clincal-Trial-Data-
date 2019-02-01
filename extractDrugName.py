import xlrd 
import nltk
import re
from nltk.tokenize import word_tokenize
#from nltk.corpus import brown
#stopwords = brown.words()

# Read in the Interventions column of the file
loc = ("0 2013-2017 Working.Inter_Drugs_Resp P_Ph_Spon_F By_Loc_45897 (201805.30.).xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(1)
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

# Process elements in each row
for i in range(1,200): 
	currDrug = sheet.cell_value(i,7)
	druglist = re.split('\|',currDrug)
	# Find out the only two types of data we want in this row
	druglist = [d for d in druglist if 'Drug' in d or 'Biological' in d]
	#print 'This is the raw data'
	#print druglist

	currDrug = ' '.join(druglist)
	druglist = re.split('\s|\/|\,|\(|\)|\%|',currDrug)
	druglist = [d for d in druglist if d.lower() not in stopwords]
	print(''.join(druglist))
for line in druglist:
	for i in range(0,len(line)):
		if line[i] == ":":
			all_drug[line[:i]] = line[i:]
print(all_drug)

