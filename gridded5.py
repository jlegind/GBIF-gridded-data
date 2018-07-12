__author__ = 'jlegind'

from decimal import Decimal
import csv
from collections import defaultdict


# Opens the csv file and selects the three columns 'datasetkey', 'decimallatitude', 'decimallongitude'
with open('G:/code_challenge/coords2.csv', 'r', encoding='utf-8') as rfile:
    reader = csv.reader(rfile, delimiter='\t')
    headers = next(reader)
    included_cols = ['datasetkey', 'decimallatitude', 'decimallongitude']

    coordict = defaultdict(list)
    # Creates a dict that takes lists as values
    for row in reader:
        line = []
        for h, r in zip(headers, row):
            if h in included_cols:
                line.append(r)
        coordict[line[0]].append(Decimal(line[1]))
        #Only appends the decimal latitude

    newcoo = coordict.copy()
    for k, v in newcoo.items():
        coordict[k] = sorted(v)
        #Sorts the coordinate values from smallest to largest. This is needed for the grid_distance function
        #Sorted() function has O(n log(n)) time complexity which is quite expensive

######## Solution #######

def grid_distance(key, num_list, pos=1, grid_limit=0.5):
    '''
    :param key: dataset key
    :param num_list: list of decimal long or lat values
    :param pos:
    :param grid_limit: assumed max step for a grid dataset
    :return: dictionary with datasetkey and a subdict with 'distance' keys and count values

    '''
    index = 1
    emitted = {key: 0}
    dd = {}
    dataset_length = len(num_list)
    print(dataset_length, 'list length')
    for j in num_list:
        while index < len(num_list):
            distance = num_list[index] - j
            if distance == 0 or distance > grid_limit : break
            elif distance not in dd:
                dd[distance] = 1
            else:
                dd[distance] += 1
            index += 1

        pos += 1
        index = pos
        emitted[key] = dd
    return emitted, dataset_length


emitted = [grid_distance(k, v, grid_limit=1) for k, v in coordict.items()]
#Object to perform calculations on
print(emitted)

for dict, dataset_length in emitted:
    for k in dict:
        tot = sum(dict[k].values())
        print("Total combinations for {} within grid-limit is: {} and original dataset length is: {}".format(k, tot, dataset_length))
        try:
            mx = max(dict[k].values())
            key_mx = max(dict[k], key=dict[k].get)
            print('Number of occurrences = {} for this distance {} '.format(mx, key_mx))
            pct = 100 * mx/dataset_length
            print('pct = {}\n'.format(round(pct, 2)))
        except ValueError:
            print("WARNING - {} likely has matching coordinates, i.e no distance\n".format(k))