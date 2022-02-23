import csv
from collections import defaultdict
from operator import length_hint
import sys

sys.setrecursionlimit(10**6)


def read_text(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    # tesing = [[10, 20], [7, 3], [30, 40]]
    next(tsv)
    dict = {}
    for node in tsv:
        diff = int(node[0]) - int(node[1])
        if diff not in dict:
            dict[diff] = [(int(node[0]), int(node[1]))]
        else:
            dict[diff].append((int(node[0]), int(node[1])))
    return dict

scores = read_text('jobs.txt')
Cj = 0
sum_of_weight = 0
check = 0
for score in sorted(scores.keys(), reverse=True):
    if len(scores[score]) > 1:
        for weight, length in sorted(scores[score], reverse=True, key=lambda x: x[0]):
            check += 1
            Cj += length
            sum_of_weight += Cj * weight
    else:
        for weight, length in sorted(scores[score], reverse=True, key=lambda x: x[0]):
            check += 1
            Cj += length
            sum_of_weight += Cj * weight

print(sum_of_weight)
print(check)