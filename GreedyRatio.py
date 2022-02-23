import csv
from collections import defaultdict
from operator import length_hint
from pickletools import long1
import sys

sys.setrecursionlimit(10**6)


def read_text(filename):
    tsv = csv.reader(open(filename), delimiter=" ")
    next(tsv)
    dict = {}
    for node in tsv:
        ratio = int(node[0]) / int(node[1])
        if ratio not in dict:
            dict[ratio] = [(int(node[0]), int(node[1]))]
        else:
            dict[ratio].append((int(node[0]), int(node[1])))
    return dict

scores = read_text('jobs.txt')
Cj = 0
sum_of_weight = 0

for score in sorted(scores.keys(), reverse=True):
    for weight, length in sorted(scores[score], reverse=True, key=lambda x: x[0]):
        print(weight, length)
        Cj += length
        sum_of_weight = sum_of_weight + (Cj * weight)
        
print(sum_of_weight)