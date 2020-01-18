# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:26:14 2019

@author: fsz537
calculate Jacksons Godfahter Index

"""
import networkx as nx
from tqdm import tqdm 

#def set_up_godfahter_index(G):
##    TOD: alternative approach:
##    consider only neighoring nodes
##    review if they 
#    out = {}
#    for x in tqdm(G.nodes()):   
#        neighbors = len(list(G.neighbors(x)))
#        triangles = nx.triangles(G,x)
#        gf = neighbors - triangles
#        
##        dict_ = { 'triangles' : triangles,
##                 'neighbors' : neighbors,
##                 'godfather_score': gf
##                 }         
##        out[x]= dict_
#        
##        (neighbors - triangles ) * neighbors
#        
#        out[x] = gf * neighbors
#        
#    return  out
#        
##temp = [n for n in G.neighbors('Armando Emilio Guebuza')]
#
#
#    
def godfathter(G):
    out = {}
    for x in tqdm(G.nodes()):
    
#  get all business partners
        first = list(set(G.neighbors(x)))
    #    consider a subgraph of only bussiness partners   
        H = G.subgraph(first)
        new_contacts = 0
        for y in first:    
    #        get the contacts a node already has
                temp = list(H.neighbors(y))
                temp = len (temp)
    #            subtrac the contact a node already and herself
                new_contacts = new_contacts + len(first) - temp - 1
    #  of a person’s friends who are not friends with each other.  
        new_contacts = new_contacts /2 
        out[x]= new_contacts
        
    return out
    
#    
#    G = subGs[2000]
#
#
#    d1 = set_up_godfahter_index(G)
#
#    d2 = godfathter(G)
#
#    ds = [d1,d2]
#    d = {}
#    for k in d1:
#        d[k] = tuple(d[k] for d in ds)
#
#    centralities = pd.DataFrame.from_dict(d, orient='index')
