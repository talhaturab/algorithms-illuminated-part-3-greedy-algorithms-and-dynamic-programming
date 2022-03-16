import csv
from collections import defaultdict
from operator import length_hint
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def read_edges(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    edges = {}
    for node in tsv:
        if int(node[2]) not in edges:
            edges[int(node[2])] = [(node[0], node[1])]
        else:
            edges[int(node[2])].append((node[0], node[1]))
    return edges

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    G = {}
    for node in tsv:
        if node[0] not in G:
            G[node[0]] = node[0]
        if node[1] not in G:
            G[node[1]] = node[1]
    return G

edges = read_edges("testkurskal.txt")
parentGraph = read_graph("testkurskal.txt")

def find(vertex, Graph):
    parent = Graph[vertex]
    while vertex != parent:
        vertex = parent
        parent = Graph[vertex]
    return parent

def union(vertex1, vertex2, graph):
    parent1 = find(vertex1, graph)
    parent2 = find(vertex2, graph)
    graph[parent2] = parent1
    return graph

x = []
for edge in sorted(edges.keys()):    
    for vertex1, vertex2 in edges[edge]:
        # print(vertex1, vertex2)
        parent1 = find(vertex1, parentGraph)
        parent2 = find(vertex2, parentGraph)
        if parent1 != parent2:
            parentGraph = union(vertex1, vertex2, parentGraph)
            x.append((vertex1, vertex2))
print(x)
        
  
  