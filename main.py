import pandas as pd
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import gmplot
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from statistics import mean
import numpy as np
import math
import random
import folium
from IPython.display import IFrame
from sklearn.manifold import TSNE
import itertools
import functionality1
import functionality2
import importlib
importlib.reload(functionality1)

def get_graph():
    G = nx.Graph()
    with open('USA-road-d.CAL.gr', 'r') as f:
        for line in f:
            if line[0] == 'a':
                n1, n2, d= list(map(int, line[2::].split()))
                G.add_edge(n1, n2, distance= d, weight= 1)

    with open('USA-road-t.CAL.gr', 'r') as f:
        for line in f:
            if line[0] == 'a':
                n1, n2, t= list(map(int, line[2::].split()))
                G[n1][n2]['time_distance'] = t

    with open('USA-road-d.CAL.co', 'r') as f:
        for line in f:
            if line[0] == 'v':
                n, lat, long = list(map(int, line[2::].split()))
                G.nodes[n]['latitude']= lat
                G.nodes[n]['longitude']= long
                G.nodes[n]['coordinates']= (lat, long)
    return G

def map_choice(G):
    print("Choose the functionality. Enter: \n -'1' to find the neighbors! \n -'2' to find the smartest network!, \n -'3' to find the shortest ordered route!, \n -'4' to find the shortest route! \n Enter 'esc' to exit", end = "")
    enter = input()
    if enter == '1':

        node=input("Choose a node ")
        measure =input('Choose a distance')
        threshold=input('Choose a threshold ')
        coordinates, distance, travel_time = functionality1.get_data()
        #Creating the graph
        l1=distance['Id_Node1']
        l2=distance['Id_Node2']
        graph = {}
        for i, j in zip(l1, l2):
            graph.setdefault(i, []).append(j)
        
        functionality1.funct1(node,measure,threshold, graph, coordinates, distance, travel_time)
        return

        
    elif enter == '2':
        network, distances, time, coordinates, weighted_network, df = functionality2.get_data()
        nodes=list(map(int,input("Choose a set of nodes (just enter the nodes id with spaces between them) ").split()))
        measure=input("Choose a distance type " )
        path = functionality2.find_smartest_path(nodes, measure, network, distances, time, coordinates, weighted_network)
        draw_graph(path,G, coordinates, df)
        gmaps(coordinates, path)
        
        
    elif enter == '3':
        print("Choose a node " , end = "")
        param1=input()
        print("Choose a sequence of nodes (just enter the nodes id with spaces between them) " , end = "")
        param2=map(int,input().split())
        print("Choose a distance type " , end = "")
        param3=input()
        #return funct3(int(param1),list(param2),str(param3))
    elif enter == '4':
        print("Choose a node " , end = "")
        param1=input()
        print("Choose a set of nodes (just enter the nodes id with spaces between them) " , end = "")
        param2=map(int,input().split())
        print("Choose a distance type " , end = "")
        param3=input()
        #return funct1(int(param1),set(param2),str(param3))
    elif enter == 'esc':
        return
    else:
        print("Please, enter again one of those: '1', '2', '3','4' or 'esc'.", '\n')
        return map_choice()

G = get_graph()
map_choice(G)