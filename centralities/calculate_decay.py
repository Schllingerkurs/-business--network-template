# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:17:01 2019

@author: fsz537

Spyder Editor

This is a temporary script file.

Decay centralitiy

  \sum_{j \neq i}   \delta^{\ell(i,j)}
  
  p ^ l 
  
  """
  
import pandas as pd
  
def set_up_decay(G):
#    TOD: alternative approach:
#    consider only neighoring nodes
#    review if they 
    out = {}
    for x in G.nodes():  
        
        first =  G.neighbors(x)
        second = []
        first = list(set(first))
        eins= len(first)
        for y in first:
            temp = G.neighbors(y)
            second.extend(temp)
        
        for w in second:
            if w in first: second.remove(w)
        second = list(set(second))

        zwei = len(second)
        third = []
        for z in second:
            temp2 = G.neighbors(z)
            third.extend(temp2)
             
        temp3 = first + second
        
        for r in third: 
            if r in temp3: third.remove(r)
        
        third = list(set(third))
                                          
        drei = len(third)
            
        f = 0.5
        dc = (f**1)*eins + (f**2) * zwei + (f**3)* drei
        
        out[x] = [eins, zwei, drei , dc ]
        
    return out
        
#test = set_up_decay(G)
#        
#        
#t = pd.DataFrame.from_dict(test, orient= 'index') 
#
##t = t.reset_index()
##
#x = 'Joao Luis Diener de Oliveira Graca Pereira'
###
###m = list(second)
###n = list(third)
###o = list (first)
#    


    
    







