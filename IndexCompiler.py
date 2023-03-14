import os
import pathlib
import json

objectList = [] # List of objects added to the list
var = 0         # Iterator for function

datasetPath = pathlib.Path(__file__).parent.resolve() #Path for parent dir

def appendToArray(dirPath, label):
    global objectList
    global var
    for entry in dirPath.iterdir():
        if(entry.is_dir()):
            for item in entry.iterdir():
                objectList.append({
                    "id": var,
                    "path": str(item),
                    "label": label
                })
                var = var + 1
        else:
            objectList.append({
                "id": var,
                "path": str(entry),
                "label": label
            })
            var = var + 1

# Start Script

for entry in datasetPath.iterdir():
    if("Ai" in entry.name):
        appendToArray(entry, "Synthetic")
    if("Human" in entry.name):
        appendToArray(entry, "Natural")

#print(str(datasetPath) + "\index.json")
json.dump(objectList, open(str(datasetPath) + "\index.json", "w"), indent=4, separators=(',',': '))