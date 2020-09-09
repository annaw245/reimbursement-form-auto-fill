# As treasurer of UBC Thunderbots, submitting reimbursement requests is an ongoing task.
# After processing them manually, I observed receipts from digikey follow a strict layout.
# Digikey is the distributor from which the electrical subteam sources their parts, accounting for 70% of the purchases.
# This is now my sixth month, and I will streamline and semi-automate this process.

from pdfminer.high_level import extract_text
import gspread

# opening the sheet
gc = gspread.service_account()
sh1 = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1W9OYU-Pw_moKfpbV9G4PgoLLqx1474criKSRsdx_w58/edit?usp=sharing')
ledger = sh1.sheet1
sh2 = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1toDU2lz_8FoDoxQGp7FqaccdyTXgevBY6fwTkXqUKLw/edit?usp=sharing')
form = sh2.sheet1

# this extracts the text from ____.pdf, which will be used to fill in the fields required on reimbursement forms
text = extract_text('testfile.pdf')

kDict = {
    # As stated above, order receipts from digikey follow a rigid format.
    # This dictionary defines the keywords to locate data we want.
    # text.find can then be used to find the starting index and end index of the string.'findName': 'Fax 218-681-3380\n',
    'findName': 'Fax 218-681-3380\n',
    'findCountry': 'CANADA',
    'findCost': 'GST on taxable amount: ',
    # Define the cell location on the form for which we want to update
    'nameCell': 'D13',
    'addressCell': 'D15',
    'totalcostCell': 'G26',
    # the indices for which the corresponding data is stored in an array
    'name': 0,
    'address': 1,
    'totalcost': 2
}

# this is the data we want to write to row. in order: Name, Date, Grand Total.
myArr = []


def updateLedger():
    # currently, all empty rows in the sheet have a astrix placeholder (*). This is because gspread lacks the functionality
    # to insert new rows. Hence we can use the worksheet.find function to determine the row number of the next empty row.
    row = ledger.find("*").row
    col = 1
    for string in myArr:
        ledger.update_cell(row, col, string)
        col = col + 1


def updateForm():
    # updates the reimbursement form
    form.update(kDict.get('nameCell'), myArr[kDict.get('name')])
    form.update(kDict.get('totalcostCell'), myArr[kDict.get('totalcost')])


# The following adds data to an array by finding the starting index of the keyphrase,
# then adding the length of the keyphrase, so as to determine the starting index of the data we want.
nameStart = text.find(kDict.get('findName')) + len(kDict.get('findName'))
nameEnd = text.find('\n', nameStart + 1)
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
updateForm()
