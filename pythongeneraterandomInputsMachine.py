#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:56:05 2019

@author: zesham2
"""

import random



    
def generateIncDecMixListRandomList(dLO,dHI,dNumofItems,sDirection):
    
    a=[]
    m=[]
    machine_list=["bublues","buParvatti","buCoumbRiyadh","buRenaisanceVector","buHyperion"]    
    for j in range(dNumofItems):
        a.append(random.randint(dLO,dHI))
        m.append(random.choice(machine_list))

    #print (m)
    print (str(m)[1:-1])
    if sDirection == "Inc":
        a.sort()
        print (str(a)[1:-1])
    elif sDirection == "Dec":
        a.sort(reverse=True)
        #print (a)
        print (str(a)[1:-1])
    elif sDirection == "Mix":
        #print (a) 
        print (str(a)[1:-1])
    
    
#print (random.randrange(10,20,3))
print ("Inc|",end=" ") 
generateIncDecMixListRandomList(10,90,30,"Inc")
print ("Dec|",end=" ") 
generateIncDecMixListRandomList(10,90,30,"Dec")
print ("Mix|",end=" ") 
generateIncDecMixListRandomList(10,90,30,"Mix")
