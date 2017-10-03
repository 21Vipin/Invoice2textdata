import json
import os
import sys
import invoice2txt

def main():
	path=sys.argv[1]
	with open(path) as f:
		config=json.load(f)
	
	if os.path.exists(config['src']):
		invoice2txt.convert(config['src'], config['des'])

if __name__ == '__main__':
	if len(sys.argv)==1:
		print("Please include the config.json file path like this - python invoice.py config.json")
	else:
		main()