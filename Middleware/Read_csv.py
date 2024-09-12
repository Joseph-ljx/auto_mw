import csv
from collections import defaultdict
import json


def read_csv():
    with open('../Database/temp.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        temp = []
        for content in csvreader:
            temp.append(content)
    # print(temp)

    CID_dict = defaultdict(list)
    for content in temp:
        if len(content) < 2:
            continue
        if not content[0]:
            continue
        CID_dict[content[4]].append(content[0])
        if content[7]:
            CID_dict[content[4]].append("alternative: " + content[7])
    # val[0] main CID, val[1] secondary CID
    return CID_dict


def read_json():
    with open('CTA_backbone.json', 'r') as j_file:
        data = json.load(j_file)
        # print(data)
    new_cid_dict = defaultdict(list)
    for circuit in data:
        if circuit['VCID']:
            new_cid_dict[circuit['VCID']].append(circuit['CTCID'])
            if circuit['Note']:
                new_cid_dict[circuit['VCID']].append(circuit['Note'])

    return new_cid_dict


if __name__ == "__main__":
    CID_dict = read_csv()
    for key, val in CID_dict.items():
        print(key, val)
    print(100*'*')
    my_new_cid_dict = read_json()
    for key, val in my_new_cid_dict.items():
        print(key, val)
