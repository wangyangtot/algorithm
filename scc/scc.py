edge={}
reversedEdge={}
vertex=[]
reversedVertex=[]

with open('scctext2.txt','r') as f:
    for line in f:
        tem=line.strip( )
        a,b=tem.split(' ')
        print a,b
        if a not in vertex:
         vertex.append(a)
         tem=[]
         tem.append(b)
         edge[a]=tem
        else:edge[a].append(b)
        if b not in reversedVertex:
            reversedVertex.append(b)
            rtem=[]
            rtem.append(a)
            reversedEdge[b]=rtem
        else:reversedEdge[b].append(a)

def initFlag():
  flag={}
  for i in vertex:
    flag[i]=False #faise present having not been traveled
  return flag


def DFS(edge,flag,vertex,stack,finishTime):

          #print edge[vertex]
          m=len(edge[vertex])
          flag[vertex]=True
          i=0
          print m
          #print flag
          while i<m and (flag[edge[vertex][i]]==True):
                print edge[vertex][i]
                i=i+1
          if i == m:
              finishTime.append(vertex)
          else:
              stack.append(vertex)
              # print stack
              # print edge[vertex][i]
              DFS(edge, flag, edge[vertex][i],stack,finishTime)



def FinishTimeOrdering(vertex,edge):
  flag=initFlag()
  stack = []
  finishTime = []
  while len(vertex) != len(finishTime):
    for i in vertex:
     if i not in finishTime:
        stack.append(i)
        while len(stack)!=0:
          tem=stack.pop()
          print tem
          DFS(edge,flag,tem,stack,finishTime)
  return finishTime


FinishTime=FinishTimeOrdering(vertex,edge)

print FinishTime

def count(finishTime):
   flag=initFlag()
   coutstack=[]
   nums=[]
   m=len(finishTime)
   i=0
   while i<m:
     if flag[finishTime[i]]==True:
         i=i+1
     else:
       num=0
       coutstack = []
       component = []
       DFS(reversedEdge,flag,finishTime[i],coutstack,FinishTime)
       print coutstack
       num=len(coutstack)+1

       nums.append(num)
   return nums

