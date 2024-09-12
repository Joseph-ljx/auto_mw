"""
Read the data from temp.csv file
* CID_dict: [Key, Value] hashmap
    1. key is a string for storing
    2. Value is an array storing multiple values. like val[0], val[1], val[2]...
    3. Return the key value map for checking
"""
import csv
from collections import defaultdict


def read_csv():
    with open('../Database/temp.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        temp = []
        for content in csvreader:
            temp.append(content)
    # print(temp)

    # Save in a hashmap dictionary (key - value):
    CID_dict = defaultdict(list)
    for content in temp:
        if len(content) < 2:
            continue
        if not content[0]:
            continue

        # Append value into an array of this key
        CID_dict[content[4]].append(content[0])

        # If there are alternative CID: val[0] main CID, val[1] secondary CID
        if content[7]:
            CID_dict[content[4]].append("Alternative: " + content[7])

    return CID_dict


# 这行代码的作用是检查当前脚本是否是直接运行的。
# 如果是直接运行的，条件为真，执行其下的代码块；如果脚本是被导入的，条件为假，代码块不会执行
# For testing:
if __name__ == "__main__":
    CID_dict = read_csv()
    for key, val in CID_dict.items():
        for value in val:
            print(key, ": " + value)

