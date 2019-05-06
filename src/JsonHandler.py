import json;


def saveObjectToJson(data, fileName):
    if fileName=='':
        fileName = 'generic.json'

    with open('src/output/'+fileName, 'w') as outfile:
        json.dump(data, outfile, indent=4)