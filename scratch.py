# As treasurer of UBC Thunderbots, submitting reimbursement requests is an ongoing task.
# After processing them manually, I observed receipts from digikey follow a strict layout.
# Digikey is the distributor from which the electrical subteam sources their parts, accounting for 70% of the purchases.
# This is now my sixth month, and I will streamline and semi-automate this process.

from pdfminer.high_level import extract_text
import gspread

# this extracts the text from ____.pdf, which will be used to fill in the fields required on reimbursement forms
text = extract_text('testfile.pdf')

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
nameEnd = text.find('\n', nameStart)
updatesheet(nameStart, nameEnd)

# the billing address immediately follows the addressee's name.
addressStart = nameEnd + 1
addressEnd = text.find(kDict.get('findCountry')) + len(kDict.get('findCountry'))
updatesheet(addressStart, addressEnd)

costStart = text.find(kDict.get('findCost')) + len(kDict.get('findCost'))
costEnd = text.find(' ', costStart)
costTotal = float(text[costStart:costEnd]) * 1.05 + float(text[costStart:costEnd]) * 0.07
print(costTotal)

text_file = open("sample1.txt", "w")
n = text_file.write(text)
text_file.close()
