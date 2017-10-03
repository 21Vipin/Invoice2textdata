import json
import os
import sys
import functions

def main():
	path=sys.argv[1]
	with open(path) as f:
		config=json.load(f)
	
	if os.path.exists(config['src']):
		functions.convert(config['src'], config['des'])

if __name__ == '__main__':
	if len(sys.argv)==1:
		print("Please include the config.json file path like this - python invoice2textdata.py config.json")
	else:
		main()
