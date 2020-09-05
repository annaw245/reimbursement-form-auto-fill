# As treasurer of UBC Thunderbots, submitting reimbursement requests is an ongoing task.
# After processing them manually, I observed receipts from digikey follow a strict layout.
# Digikey is the distributor from which the electrical subteam sources their parts, accounting for 70% of the purchases.
# This is now my sixth month, and I will streamline and semi-automate this process.

from pdfminer.high_level import extract_text
import gspread
import numpy as np

# opening the sheet using
gc = gspread.service_account()
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1W9OYU-Pw_moKfpbV9G4PgoLLqx1474criKSRsdx_w58/edit#gid=0')
worksheet = sh.sheet1

# this extracts the text from ____.pdf, which will be used to fill in the fields required on reimbursement forms
text = extract_text('testfile.pdf')

# As stated above, order receipts from digikey follow a rigid format.
# This dictionary defines the keywords to locate data we want.
# text.find can then be used to find the starting index and end index of the string.
kDict = {'findName': 'Fax 218-681-3380\n',
         'findCountry': 'CANADA',
         'findCost': 'GST on taxable amount: '}

# this is the data we want to write to row. in order: Name, Date, Grand Total.
myArr = []


# this updates the google sheet on which the form is located
def updateArray(start, end):
    myArr.append(text[start:end])


def updateLedger():
    # currently, all empty rows in the sheet have a astrix placeholder (*). This is because gspread lacks the functionality
    # to insert new rows. Hence we can use the worksheet.find function to determine the row number of the next empty row.
    row = worksheet.find("*").row
    col = 1
    for string in myArr:
        worksheet.update_cell(row, col, string)
        col = col + 1


# this is the starting index of the billing name. It finds the starting index of the keyphrase,
# then adds the length of the keyphrase.
nameStart = text.find(kDict.get('findName')) + len(kDict.get('findName'))
nameEnd = text.find('\n', nameStart+1)
myArr.append(text[nameStart:nameEnd])

# the billing address immediately follows the addressee's name.
addressStart = nameEnd + 1
addressEnd = text.find(kDict.get('findCountry')) + len(kDict.get('findCountry'))
myArr.append(text[addressStart:addressEnd])

costStart = text.find(kDict.get('findCost')) + len(kDict.get('findCost'))
costEnd = text.find(' ', costStart)
costTotal = float(text[costStart:costEnd]) * 1.05 + float(text[costStart:costEnd]) * 0.07
myArr.append(costTotal)

updateLedger()

text_file = open("sample1.txt", "w")
n = text_file.write(text)
text_file.close()
