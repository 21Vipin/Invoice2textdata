
import os
import sys
import string
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter

def convert(src, des):
    for root, dirs, files in os.walk(src):
        try:
            for file in files:
                if file.endswith(".pdf"):
                    if not file.startswith("._"):
                        outfile = des
                        codec = 'utf-8'
                        caching = True
                        rsrcmgr = PDFResourceManager(caching=caching)
                        if outfile:
                            outfp = open(outfile, 'wt', encoding=codec, errors='ignore')
                            close_outfp = True
                        else:
                            outfp = sys.stdout
                            close_outfp = False
                        device = TextConverter(rsrcmgr, outfp)
                        fname = os.path.join(root, file)
                        fp = open(fname, 'rb')
                        process_pdf(rsrcmgr, device, fp, check_extractable=True)
                        fp.close()
                        device.close()
                        if close_outfp:
                            outfp.close()
                        test=open(outfile).read()
                        invoice=find_invoice_number(test)
                        date= find_date(test)
                        due_amount = find_amount(test)
                        print("{ File Name: ", file, "Invoice Number: ", invoice, "Invoice Date: ", date, "Due Amount: Rs ", due_amount,"}")
        except:
            print('An error occured.')

                    
def find_invoice_number(str):
	str_lower = str.lower()
	index = 0
	while index < len(str_lower):
		index = str_lower.find('invoice', index)
		if index == -1:
			break
		if "no" in str_lower[index + 7: index + 10] or "number" in str_lower[index + 7: index + 14]:			#randomly printing 40 characters starting from invoice
			str = str[index + 10: index + 30]								#stripping string to less characters
			
			#check for actual invoice number
			if "INV" in str:												#invoice with INV
				start = str.find("INV") + 3
				invoice = 'INV'
			else:
				for pos,char in enumerate(str):
					if char.isdigit():
						start = pos											#starting index for invoice
						invoice = ''
						break
			
			for pos,char in enumerate(str[start:]):
				if char in string.punctuation:
					continue
				if char.isalpha():
					end = pos												#ending index for invoice
					break
			invoice = invoice + str[start: start + end]
			return invoice
			
		index += 7 # +7 because len('invoice') == 7							#to check for all 'invoice' keywords

def find_date(str):
	str_lower = str.lower()
	index = 0
	while index < len(str_lower):
		index = str_lower.find('date', index)
		if index == -1:
			break
		start=0
		end = 0
		date=''
		if ":" in str_lower[index + 4: index + 12]:			
			str = str[index + 4: index + 25] 
			months = ["Jan", "Feb", "Mar", "Apr", "May" , "Jun" , "Jul" ,"Aug" , "Sep" , "Oct" , "Nov" , "Dec"]
			for month in months:
				if month in str:												
					start = str.find(month) - 3
					end= start + 10
					break
				else:
					for pos,char in enumerate(str):   
						if char.isdigit():
							start = pos
							end =  10
							break
			date = date + str[start: start + end]
			return date
		else:
			str = str[index + 4:]
			months = ["January", "February", "March", "April", "May" , "June" , "July" ,"August" , "September" , "October" , "November" , "December"]
			for month in months:
				if month in str:												
					start = str.find(month) + len(month)
					date = month

			for pos,char in enumerate(str[start:]):
				if char.isalpha():
					end = pos												
					break
			
			date = date + str[start: start + end]
			return date
			
		index += 7 

def find_amount(str):
	str_lower = str.lower()
	index = 0
	start=0
	end=0
	while index < len(str_lower):
		index = str_lower.find('balance', index)
		if index == -1:
			break
		if "due" in str_lower[index + 7:]:
			str = str[index + 12: index + 30 ]								
			for pos,char in enumerate(str):
					if char.isdigit():
						start = pos + 1										
						invoice =""
						break	
			for pos,char in enumerate(str[start:]):
				if char.isalpha():
					end = pos												
					break
			invoice = invoice + str[start: start + end]
			return invoice
		index += 7 		