import json

import ngxTranslateFlattener

with open('de.json', 'r', encoding="utf-8") as file:
  data = json.load(file)

flattened_data = ngxTranslateFlattener.flatten(data)

with open('result.csv', 'w', encoding="utf-8") as resultFile:
  resultFile.write("Key;DE;FR;\n")
  for key in flattened_data.keys():
    resultFile.write("%s;%s;;\n" % (key, flattened_data[key]))
