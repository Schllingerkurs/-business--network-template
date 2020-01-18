# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:53:12 2019

@author: fsz537

calculate_centralities


Input: dict of G  (each key is  a time period)
Output: centralities 

Issue: scaling needs to be adjusted for output. Devide by max value in column .
"""

from multiprocessing import Pool
import networkx as nx
import pandas as pd
import glob
import os
from sklearn import preprocessing
import pickle
import time

os.chdir(r'H:\MozBiz\Python\centralities')

# own modules
import subggraphs_by_year as sgby
import calculate_godfahter as gf
import calc_decay as calcd

def load_Graph(years_time):
        
    list_of_files = glob.glob(r'H:\MozBiz\Data\workingdata\graphs\*')
    latest_file = max(list_of_files, key=os.path.getctime)
    G = nx.read_gpickle(latest_file)
    subGs = sgby.graphs_by_time_dict(G, years_time)    
    return subGs
 
def collect_centralities(inp,x):
    year = x
    print(year)
    G = inp
#    d1 = nx.degree_centrality(G)
#    print('degree done', year)
##    becomes a very advanced calculation. Use Jacson´s(2019) Godfather index to compensate
#    d2 = nx.betweenness_centrality(G)  
#    print('betweenness_centrality done' , year)
##    d3=  nx.eigenvector_centrality(G)
##    print ('eigenvector_centrality done', year)
#    d4 = (nx.closeness_centrality(G))
#    print('closeness_centrality done', year)   
    d5 = gf.godfathter(G)
    print('godfather done', year)
    d6 = calcd.set_up_decay(G)
    print ("decay done", year)
#d2,
#    ds = [d1,  d3, d4, d5, d6]   
    ds = [d5,d6]
    d = {}
    for k in d5:
        d[k] = tuple(d[k] for d in ds)
    centralities = pd.DataFrame.from_dict(d, orient='index')
#    centralities.columns = ['c_dgr','c_btwnn',
#                             'c_eign',
#                             'c_clsn',
#                             'c_gf',"c_decay"]
    centralities.columns = ['c_gf',"c_decay"]  
    
    return centralities


def parallel_collect(graph_dict):
    
    inputlist = zip(graph_dict.keys(), graph_dict.values())

    outdict = {}
    with Pool(6) as pool:
        results = pool.map(collect_centralities, [x for x in inputlist])
        
        for year, cent in results:
            outdict[year] = cent
                       
    return outdict
    

def set_up_centralities_by_year(subgraph):
      
    centralities = {}
    for x in subgraph.keys():
        centralities[x]= collect_centralities(subgraph[x],x)
       
    centralities_all = pd.DataFrame()
    for x in centralities.keys():   
        df = centralities[x]
        df['year'] = x
        centralities_all = centralities_all.append(df)
    return centralities_all

#def normalize_centralities(centralities, years_time):
##    normalize centralities with sklearn  preprocessing 
#    
#    df_out = pd.DataFrame()
#    for y in years_time:  
#        c_90 = centralities[centralities['year']== y] 
#        index_names = c_90.reset_index()[['index']]
#        c_90= c_90[['degree',"betweenness",
#                             'eigenvector','closeness']]
#        
#        x = c_90.values
#        min_max_scaler = preprocessing.MinMaxScaler()
#        x_scaled = min_max_scaler.fit_transform(x)
#        df = pd.DataFrame(x_scaled)
#        df.columns=['degree',"betweenness",'eigenvector','closeness']
#        df['year'] = y  
#        df = df.merge(index_names, left_index= True, right_index = True, how='inner')
#        df = df.set_index('index')
#          
#        df_out = df_out.append(df) 
#           
#    return df_out

def save_centratlities(centralities):
    
    timestr = time.strftime("%y%m%d")    
    path = r'H:\MozBiz\Data\workingdata\centralities\cntrlts'
    with open(path + timestr+'.pickle', 'wb') as f:     
         pickle.dump(centralities, f, protocol = 4)         
    return 
    
def main():
    
    years_time = range (1994,2020,5)
  
    subGs  = load_Graph(years_time) 
    print('graphs')
#    out = parallel_collect(subGs)
    centralities_all = set_up_centralities_by_year(subGs)

# leave out normalization for now , done in stata    
#    centralities_all = normalize_centralities(centralities_all, years_time)   
    
    
#    cntrlts = set_up_centralities_by_year(out)
                               
#   map centralities to frame
#    cntrlts= cntrlts.reset_index()
    
    cntrlts = centralities_all
#    
    cntrlts[['prtnr1', 'prtnr2','prtnr3','decay']] = pd.DataFrame(cntrlts.c_decay.values.tolist(), index= cntrlts.index)
#    cntrlts = cntrlts.drop(columns=['c_decay'])
    save_centratlities(cntrlts)
        

if __name__ == "__main__":
    main()



#    info = nx.info(subGs[2015])♠







