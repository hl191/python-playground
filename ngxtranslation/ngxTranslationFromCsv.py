import csv
import json

import ngxTranslateFlattener

data = {}
with open('result.csv', 'r', encoding="utf-8") as file:
  reader = csv.DictReader(file, delimiter=';')
  for row in reader:
    id = row['Key']
    data[id] = row['ITA']

unflattened = ngxTranslateFlattener.unflatten(data)

with open('imported.json', 'w', encoding="utf-8") as resultFile:
  resultFile.write(json.dumps(unflattened, indent=4))
