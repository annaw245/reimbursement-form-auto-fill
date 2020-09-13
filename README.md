# Reimbursement Form and Ledger Autofill

### Motivation

As treasurer of UBC Thunderbots, I frequently submit reimbursement requests on behalf of other members. After processing them manually, I observed that most reciepts follow a strict layout. With a combination of text extraction from the reciepts and simple excel functions, I can automatically fill in the 70% of the reimbursement form and 100% of our ledger. 

## Explanation 

I used [pdfminer.six](https://github.com/pdfminer/pdfminer.six) which extracts text from the pdf reciept. Then, I manipulate the string to obtain relevant information. Using [gspread](https://gspread.readthedocs.io/en/latest/) API, the data is written to designated cells on a google sheets via a service account.

## Requirements

Install the following with pip.
```
pip install gspread
```
```
pip install pdfminer.six
```
## Demo
