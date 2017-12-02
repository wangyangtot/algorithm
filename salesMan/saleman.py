import numpy as np
import math
from collections import defaultdict

class salesman:
    def __init__(self,graphfile):

        with open(graphfile,'r') as f:
            self.num_cities=int(f.readline())
            #print num_cities
            self.coordinates=[]
            self.set=[]
            self.path = defaultdict(dict)
            for city in range(self.num_cities):
             self.coordinates.append([float(tem) for tem in f.readline().strip().split(" ")])

        self.dis=np.zeros((self.num_cities,self.num_cities))
        for fromcity in range(self.num_cities):
            self.set.append(fromcity)
            for tocity in range(self.num_cities):
                a=math.pow((self.coordinates[fromcity][0]-self.coordinates[tocity][0]),2)
                b=math.pow((self.coordinates[fromcity][1]-self.coordinates[tocity][1]),2)
                self.dis[(fromcity, tocity)]=math.sqrt(a+b)

        print self.dis
        print self.set

    def hashlist(self,list):
        if not list:
            #print list
            return 'none'
        else:
            return ''.join(str(x) for x in list)

    def tsp(self,source,set):


         #print set

         if not set:
              self.path[source]['none']=self.dis[0][source]
              #print self.path

         else:
              temdic = {}
              for j in set:
                  #print j
                  temset=list(set)
                  temset.remove(j)
                  #print j, temset
                  self.tsp(j,temset)
                  #print set
              for j in set:
                  temset=list(set)
                  temset.remove(j)
                  #print temset
                  index=self.hashlist(temset)
                  #print source
                  #print temset,j
                  temdic[j]=self.path[j].get(index)+self.dis[j][source]
                  #print temdic[j]

              minkey=min(temdic,key=temdic.get)
              #print minkey
              #print set
              minpath=temdic[minkey]
              #set.remove(minkey)
              index=self.hashlist(set)
              #print index
              self.path[source][index]=minpath
         #print self.path
    def run(self):
        self.set.remove(0)
        self.tsp(0,self.set)


a=salesman('input_float_56_15.txt')
a.run()
print a.path


