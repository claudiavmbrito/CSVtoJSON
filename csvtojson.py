import csv
import sys
import json


fields=["timestamp","channel 1","channel 2"]

def conversor(filename):
  csv_filename = filename[0]
  print("Opening CSV file: " + csv_filename)
  with open(csv_filename, 'r') as f:
    csv_reader = csv.DictReader(f,fields)
    json_filename = csv_filename.split(".")[0]+".json"
    print("Saving JSON to file: " + json_filename)
    with open(json_filename,'w') as jsonf:
      for r in csv_reader:
        data = json.dumps(r)
        jsonf.write(data)
      
      f.close()
      jsonf.close()

if __name__=="__main__":
  conversor(sys.argv[1:])