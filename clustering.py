from cgitb import small
from cmath import inf
import csv
from collections import defaultdict
from operator import length_hint
import sys

sys.setrecursionlimit(10**6)

def read_edges(filename):
    # Read an undirected edges in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    next(tsv)
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
    next(tsv)
    G = {}
    for node in tsv:
        if node[0] not in G:
            G[node[0]] = node[0]
        if node[1] not in G:
            G[node[1]] = node[1]
    return G

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

def clustering(edges, parentGraph, k):
    clusters = len(parentGraph)
    for length, endpoints in sorted(edges.items(),  key=lambda x: x[0]):    
        for vertex1, vertex2 in endpoints:
            parent1 = find(vertex1, parentGraph)
            parent2 = find(vertex2, parentGraph)
            if parent1 != parent2:
                clusters -= 1
                parentGraph = union(vertex1, vertex2, parentGraph)
                x.append((vertex1, vertex2))
                if clusters == k:
                    break
        if clusters == k:
            break
    
    smallest = inf
    for length, endpoints in sorted(edges.items(),  key=lambda x: x[0]):
        for vertex1, vertex2 in endpoints:
            parent1 = find(vertex1, parentGraph)
            parent2 = find(vertex2, parentGraph)
            if parent1 != parent2:
                if length < smallest:
                    smallest = length
    print(smallest)

x = []
edges = read_edges("clustering1.txt")
parentGraph = read_graph("clustering1.txt")
clustering(edges, parentGraph, 4)
parentGraph