# As treasurer of UBC Thunderbots, submitting reimbursement requests is an ongoing task.
# After processing them manually, I observed receipts from digikey follow a strict layout.
# Digikey is the distributor from which the electrical subteam sources their parts, accounting for 70% of the purchases.
# This is now my sixth month, and I will streamline and semi-automate this process.

from pdfminer.high_level import extract_text
import gspread

# this extracts the text from ____.pdf, which will be used to fill in the fields required on reimbursement forms
text = extract_text('testfile.pdf')

<<<<<<< HEAD
# As stated above, order receipts from digikey follow a rigid format.
# This dictionary defines the keywords to locate data we want.
# text.find can then be used to find the starting index and end index of the string.
kDict = {'findName': 'Fax 218-681-3380\n',
         'findCountry': 'CANADA',
         'findCost': 'GST on taxable amount: '}


# this updates the google sheet on which the form is located
def updatesheet(start, end):
    print(text[start:end])
    return 0


# this is the starting index of the billing name. It finds the starting index of the keyphrase,
# then adds the length of the keyphrase.
nameStart = text.find(kDict.get('findName')) + len(kDict.get('findName'))
=======
# order receipts from digikey follow a rigid format. This dictionary defines the keywords preceding data we want
# eg. name.
kDict = {'findName': 'Fax 218-681-3380',
         'country': 'Canada',
         'findTotal': 'GST on taxable amount:'}

# this is the starting index of the data we want. It finds the starting index of the keyphrase,
# then adds the length of the keyphrase. +2 to account for the line break
nameStart = text.find(kDict.get('findName')) + len(kDict.get('findName')) + 2
>>>>>>> parent of 6d4cc56... added text detection for address and total cost
nameEnd = text.find('\n', nameStart)
print(text[nameStart:nameEnd])


<<<<<<< HEAD
costStart = text.find(kDict.get('findCost')) + len(kDict.get('findCost'))
costEnd = text.find(' ', costStart)
costTotal = float(text[costStart:costEnd]) * 1.05 + float(text[costStart:costEnd]) * 0.07
print(costTotal)
=======
>>>>>>> parent of 6d4cc56... added text detection for address and total cost

text_file = open("sample1.txt", "w")
n = text_file.write(text)
text_file.close()
