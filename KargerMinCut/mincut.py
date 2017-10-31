import random
from random import shuffle

f=open('KargerMinCut.txt','rU')
l=f.read().strip(" ")
x=l.split('\n')   #spilt lines
Karger_array={}
for index in range(len(x)):
     line=(x[index].split('\t')) #split elements in every line
     line=line[:-1]  #del the last element which is " " at the end of  each line
     Karger_array[line[0]]=line[1:]
def make_edge(array):
 m=len(array)
 edge=[]
 for key in array:
    N=len(array[key])
    for j in range(N):
     edge.append((key,array[key][j]))
 return edge

def contract(array,edge):

     tem = random.choice(edge)
     node1=tem[0]
     node2=tem[1]
                       #contract the node_a and node_b,delete node_b
     for i in array[node2]:
                  if i!=node1:array[node1].append(i) #transfer the edges of node2 to the node1
                  if i!=node1: array[i].append(node1)
                  array[i].remove(node2)

                          #delete the node2 from the edge_list of node1
     del array[node2]
     return array

def Random_contract(array):
  m=len(array)
  while m>2:
     edge = make_edge(array)
     array=contract(array, edge)
     m=len(array)
  key1=array.keys()[0]
  return len(array[key1])
#print Karger_array
#edge=make_edge(Karger_array)
#print edge
a={'1':['2','3'],'2':['1','4','3'],'3':['1','4','2'],'4':['2','3']}

#num=Random_contract(Karger_array)
#print num
sum=0
for i in range(100):#repeat numbers
    num=Random_contract(Karger_array)
    print num


