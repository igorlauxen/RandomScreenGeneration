import json;


def saveObjectToJson(data, fileName):
    if fileName=='':
        fileName = 'generic.json'

    result = []
    for single_data in data:
        result.append(single_data.serialize())

    with open(fileName, 'w') as outfile:
        s = json.dumps(result)
        json.dump(s, outfile, indent=4)