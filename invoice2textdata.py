import json
import os
import sys
import functions
import zipfile

def main():
    path=sys.argv[1]
    with open(path) as f:
        config=json.load(f)
    
    # unzip the zip file
    zip_ref = zipfile.ZipFile(config['zip'], 'r')
    zip_ref.extractall(config['src'])
    zip_ref.close()
    
	
    if os.path.exists(config['src']):
        functions.convert(config['src'], config['des'])

if __name__ == '__main__':
    if len(sys.argv)==1:
        print("Please include the config.json file path like this - python invoice2textdata.py config.json")
    else:
        main()
