#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:56:05 2019

@author: zesham2
"""

import random
import datetime
from random import randrange

NUMITEMS=100
CONTROL_FLIP=0


def random_date(start,l):
   current = start
   while l >= 0:
      curr = current + datetime.timedelta(minutes=randrange(60))
      yield curr
      l-=1

startDate = datetime.datetime(2013, 9, 20,random.randint(1,23),00)
timeslist=[]

"""
for x in random_date(startDate,10):
    y = datetime.datetime(2013, 9, 20,random.randint(1,23),random.randint(1,59))
    #print  (x.strftime("%H:%M") )
    #print  (y.strftime("%H:%M") )
    timeslist.append( y.strftime("%H:%M"))

print (",".join(timeslist))

"""



    

def generateIncDecMixListRandomList(dLO,dHI,dNumofItems,sDirection,CONTROL_FLIP):
    
    a=[]
    m=[]
    machine_list=["bublues","buParvatti","buCoumbRiyadh","buRenaisanceVector","buHyperion"]    
    randtimeslist=[]
  

    for j in range(dNumofItems):
        randtime = datetime.datetime(2013, 9, 20,random.randint(1,23),random.randint(1,59))
        a.append(random.randint(dLO,dHI))
        m.append(random.choice(machine_list))
        randtimeslist.append(randtime.strftime("%H%M"))

    #print (m)
    if (CONTROL_FLIP==0): 
    	randtimeslist.insert(0, "Times")
    	print (",".join(randtimeslist))
    	m.insert(0,"MachinesNames")
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
print ("1.IncCPU|",end=" ") 
generateIncDecMixListRandomList(10,90,NUMITEMS,"Inc",0)
print ("1.IncMEM|",end=" ") 
generateIncDecMixListRandomList(10,90,NUMITEMS,"Inc",1)
print ("2.DecCPU|",end=" ") 
generateIncDecMixListRandomList(10,90,NUMITEMS,"Dec",1)
print ("2.DecMEM|",end=" ") 
generateIncDecMixListRandomList(10,90,NUMITEMS,"Dec",1)
print ("3.MixCPU|",end=" ") 
generateIncDecMixListRandomList(10,90,NUMITEMS,"Mix",1)
print ("3.MixMEM|",end=" ") 
generateIncDecMixListRandomList(10,90,NUMITEMS,"Mix",1)
