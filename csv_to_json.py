
import sys;
import json;
from json import JSONEncoder;
from os.path import basename;
from pprint import pprint;

class objectConversion(object):
	pass

def getFileNameAtomic(fileName):
	splits = fileName.split(".");
	newName = "";
	for i in range(0, len(splits)-1):
		newName += splits[i] + ".";
	return newName;

# -- Functions
def csv_to_json(fileNameCSV):
	# Read File
	readFile = open(fileNameCSV, "r");
	# Write File
	fileNameJSON = getFileNameAtomic(fileNameCSV) + "json";
	writeFile = open(fileNameJSON, "w");
	# Get fields of CSV
	firstLine = readFile.readline();
	fields = firstLine.split(",");
	fields[len(fields)-1] = fields[len(fields)-1].split("\n")[0];

	j = 0;


	objects = [];
	# Each Entities
	for line in readFile:
		values = line.split(",");
		values[len(values)-1] = values[len(values)-1].split("\n")[0];
		# Write an entitie
		objectValue = objectConversion();
		for i in range(0, len(fields)):
			setattr(objectValue, fields[i], values[i]);
		objects.append(objectValue.__dict__);
	jsonValue = json.dumps(objects, sort_keys=True, indent=4);
	writeFile.write(jsonValue);

if len(sys.argv) < 2:
	sys.exit("Pas les bons arguments.");

for i in range(1, len(sys.argv)):
	csv_to_json(sys.argv[i]);
