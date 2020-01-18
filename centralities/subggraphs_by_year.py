# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:53:11 2019

@author: fsz537

create subgraphs
"""

import networkx as nx
import pandas as pd 

def set_up_edges_by_time(G, years_time):
    edges_year = nx.get_edge_attributes(G,'year')
    edges_year = pd.DataFrame.from_dict(edges_year, orient = 'index', columns =['year'])
    out = {}
    for x in years_time:
            matches = edges_year.loc[ edges_year['year']<x]
            out[x] = matches
    return out



def create_subgraphs(out,G):
    subgraph = {}

    for x in out.keys():
        Gc = nx.Graph()
        Gc.add_nodes_from(G.nodes)
        Gc.add_edges_from(out[x].index.tolist())
        subgraph[x] = Gc

    return subgraph


def graphs_by_time_dict(G,years_time):
#subgrapah of 
    out = set_up_edges_by_time(G, years_time)
    
    subgraph = create_subgraphs(out,G)
    
    return subgraph




