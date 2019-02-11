import PyPDF2
import re
import functools

pdfFileObj = open('January 15.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages

pageObj = pdfReader.getPage(2)
pdf_text = pageObj.extractText()

#print(pdf_text)


regex = "[\d]{2}/[\d]{4}/[\d]{2}"
start_index = re.search(regex, pdf_text).start()
end_index = pdf_text.index('Date', 100)
#print(start_index)
#print(end_index)

new_text = pdf_text[start_index:end_index]

#print(new_text)
#split each transaction by date
regex2 = "([\d]{2}/[\d]{4}/[\d]{2})"


split_string = re.split(regex2, new_text)
#print(split_string)


#cleanup
filtered_list = list((filter(None, split_string)))
#print(filtered_list)


regex3 = "[\d]{2}/[\d]{4}/[\d]{2}"
date_list = []
desc_list = []
for i in filtered_list:
	if re.match(regex3, i):
		date_list.append(i[:5])
	else:
		desc_list.append(i)
			
results = zip(date_list, desc_list)
#print(list(results))

date_join_set = []
for i in results:
	date_join = ' '.join(i)
	date_join_set.append(date_join)
	
#print(date_join_set)

#white_space_removal 
white_space = []
for i in date_join_set:
	new_line = ' '.join(i.split())
	white_space.append(new_line)

#print(white_space)

dollar_sign = []
for i in white_space:
	dsign = i.replace('$', ' $')
	dollar_sign.append(dsign)

final_set = []
for i in dollar_sign:
	first = i.split(' ', 1)
	desc = first.pop(1).rsplit(' ',1)
	date = first.pop().rsplit(' ', 1)
	final = date + desc
	#first_split.append(first)
	final_set.append(final)
	
#print(first_set)

for i in final_set:
	new_desc = i[1].replace(' ', '')
	amount = i[2].replace('$', '')
	print(','.join([i[0], new_desc, amount]))
