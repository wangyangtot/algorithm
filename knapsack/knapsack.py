import numpy as np
from numpy import linalg
import time

class knapsack():
    def __init__(self,file):
        self.item={}

        with open(file,'r') as f:
            self.capacity,self.num_item=(int(tem) for tem in f.readline().split(" "))
            self.cache = np.zeros((self.num_item,self.capacity+1))
            for i in range(1,self.num_item+1):
                value,weight=(int(tem) for tem in f.readline().split(" "))
                self.item[i]=[value,weight]
            self.item[0]=0,0
            #print self.item
    '''def cache_grow(self):
        tem=self.item[0][1]
        self.cache[0][tem:]=self.item[0][0]
        #print self.cache
        for i in range(1,self.num_item):
            for j in range(self.capacity+1):
                if  j-self.item[i][1]<0:
                    self.cache[i][j] = max(self.cache[i - 1][j],0)
                else:
                 self.cache[i][j]=max(self.cache[i-1][j],self.cache[i-1][j-self.item[i][1]]+self.item[i][0])'''

    def get_max_value(self):
        return self.cache[self.num_item-1][self.capacity]
    def bigCacheGrow(self):

        def search_root(i,j):
            #print i,j
            if (all(map(lambda x,y: x == y, (i,j),self.root[(i,j)]))):
                return i,j
            else:
                temnum,temvalue=self.root[(i,j)]
                return search_root(temnum,temvalue)

        self.bigCache={}
        self.root={} #save the  keys of dic to remove the redundancy
        for num in range(0,self.num_item+1):
            for weight in range(self.capacity+1):
             self.root[(num,weight)]=num,weight
             #self.bigCache[(num,weight)]=0
        #print self.root
        #print self.bigCache

        for num in range(1,self.num_item+1):
            for weight in range(1,self.capacity+1):
                #print ('num',num,"fill",weight,":")
                if weight<self.item[num][1]:
                    self.root[(num,weight)]=num-1,weight
                else:
                    root1=search_root(num-1,weight-self.item[num][1])
                    root2=search_root(num-1,weight)
                    #print root1, root2
                    sum1= self.bigCache.get(root1,0)+self.item[num][0]
                    sum2=self.bigCache.get(root2,0)
                    #print sum1,sum2
                    if sum1<=sum2:
                        self.root[(num,weight)]=root2
                    else:self.bigCache[(num,weight)]=sum1
                #print self.bigCache[(num,weight)]
                #print self.root[(num,weight)]
        print self.bigCache[(self.num_item,self.capacity)]

start=time.time()
a=knapsack('knapsack_big.txt')
a.bigCacheGrow()
end=time.time()
print(end-start)
#print a.bigCache[(4,4)]
#answer is 2493893 time:10.3290379047