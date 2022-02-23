from cmath import inf
import csv

def make_link(G, node1, node2, length):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = length
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = length
    return G

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter=" ")
    next(tsv)
    G = {}
    for node in tsv:
        make_link(G, node[0], node[1], int(node[2]))
    return G

def prim(G, start_vertex):
    cost_of_graph = 0
    processed = [start_vertex]
    open_list = [start_vertex]
    while len(open_list) > 0:
        minValue = inf
        minVertex = ""
        for vertex in open_list:
            Isprocessed = True
            for neighbour in G[vertex].keys():
                if neighbour not in processed:
                    Isprocessed = False
                    if G[vertex][neighbour] < minValue:
                        minVertex = neighbour
                        minValue = G[vertex][neighbour]
   
        if Isprocessed:
            open_list.remove(vertex)
        else:
            processed.append(minVertex)
            open_list.append(minVertex)
            cost_of_graph += minValue

    print(cost_of_graph)


G = read_graph("edges.txt")
prim(G, "1")