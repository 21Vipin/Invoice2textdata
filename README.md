# Invoice2textdata
PDFs are extremely difficult to scrape. Converting them to text files can make extracting their data significantly easier. I have focused on the widely used pdfminer package from python. 

Convert from PDF files to this:

        { File Name:  2112.pdf Invoice Number:  INV002112 Invoice Date:  13-Jun-2016 Due Amount: Rs  1,661.09 }
        { File Name:  2137.pdf Invoice Number:  INV002137 Invoice Date:  22-Jun-2016 Due Amount: Rs  45.76 }
        { File Name:  2138.pdf Invoice Number:  INV002138 Invoice Date:  22-Jun-2016 Due Amount: Rs  45.76 }

# Prerequisite
Update the config.json file and set the path as shown bellow:
        
        "src" : "Path where the zip file will be exctracted.",
        "des" : "path to the text file in which the complete data of pdf is exctracted.",
        "zip" : "complete path to the where the zip file is."

# Execution     
To extract the data from the set of pdf files, the invoive2textdata.py file is executed with the help of command: 

                                python invoive2textdata.py config.json  

# Usage
invoice2textdata.py : Is used to convert the file to text and find File Name, Invoice number, Invoice 
                      date, Due amount.
                      
functions.py        : Has set of functions like:
                        1. convert(), 
                        2. find_invoice_number(), 
                        3. find_date(),
                        4. find_amount()
                        
config.json         : Has path to Source and Destination.

 
