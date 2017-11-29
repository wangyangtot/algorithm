import math
from collections import defaultdict
class AllPairsShortestPath:
    def __init__(self,graphfile):
        self.short_dis = {}
        self.toHead = defaultdict(list)
        with open(graphfile) as f:
            self.num_vertex,num_edges=(int(tem) for tem in f.readline().split(" "))
            for line in f:
                tail,head,value=(int(tem) for tem in line.split(' '))
                self.toHead[tail].append((head,value))
        print self.toHead

    def _init_shortestPath(self,initNumber):
        for i in  range(1,self.num_vertex+1):
            self.short_dis[i]=initNumber



    def update(self,previous_vertexs):
        next_vertexs=set()
        for vertex in previous_vertexs:
             for tem  in self.toHead[vertex]:
                 next_vertexs.add(tem[0])
                 self.short_dis[tem[0]]=min(self.short_dis[vertex]+tem[1],self.short_dis[tem[0]])
        return next_vertexs

    def BellmanFord(self):
        self._init_shortestPath(0)
        previous_vertexs=(tem for tem in range(1,self.num_vertex))
        for num in range(self.num_vertex):
            previous_shortpath = self.short_dis.copy() #implicitly copies objects instead of  the copy of pointer
            next_vertexs=self.update(previous_vertexs)
            if not next_vertexs:break
            else:
                previous_vertexs=next_vertexs
        if previous_shortpath!=self.short_dis:
            return None
        else:
            shortestvertex=min(self.short_dis,key=self.short_dis.get)
            return shortestvertex,self.short_dis[shortestvertex]



if __name__=="__main__":
    a=AllPairsShortestPath("input_random_44_2048.txt")
    b=a.BellmanFord()
    print b


