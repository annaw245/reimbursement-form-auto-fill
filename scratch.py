from pdfminer.high_level import extract_text

# this extracts the text from ____.pdf, which will be used to fill in the fields required on reimbursement forms
text = extract_text('testfile2.pdf')

# order receipts from digikey follow a rigid format. This dictionary defines the keywords preceding data we want
# eg. name.
kDict = {'findName': 'Fax 218-681-3380',
         'country': 'Canada',
         'findTotal': 'GST on taxable amount:'}

# this is the starting index of the data we want. It finds the starting index of the keyphrase,
# then adds the length of the keyphrase. +2 to account for the line break
nameStart = text.find(kDict.get('findName')) + len(kDict.get('findName')) + 2
nameEnd = text.find('\n', nameStart)
print(text[nameStart:nameEnd])



text_file = open("sample2.txt", "w")
n = text_file.write(text)
text_file.close()
