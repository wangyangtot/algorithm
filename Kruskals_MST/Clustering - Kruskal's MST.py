from collections import defaultdict

class union_find:
  def __init__(self, num):
          self._root = {}
          self._clusterSize = {}
          for i in range(1, num + 1):
              self._root[i] = i
              self._clusterSize[i] = 1

  def _findroot(self,node):
      tem=node
      while self._root[tem]!=tem:
            self._root[tem]=self._root[self._root[tem]]
            tem=self._root[tem]
      return tem
  def get_root(self):
      return self._root
  def get_clustersize(self):
      return self._clusterSize

  def union(self,node1,node2):
     root_node1=self._findroot(node1)
     root_node2=self._findroot(node2)
     if root_node1==root_node2:return
     else:
      if self._clusterSize[root_node1]>self._clusterSize[root_node2]:
         self._root[root_node2]=root_node1

         self._clusterSize[root_node1]+=self._clusterSize[root_node2]
         self._clusterSize[root_node2]=0
      else:
          self._root[root_node1]=root_node2
          self._clusterSize[root_node2] += self._clusterSize[root_node1]
          self._clusterSize[root_node1]=0

  def num_cluster(self):
      num=0
      for key, value in self._root.items():
          if key == value:
              num += 1
      return num

class clustering():
    def __init__(self,graph_file):
        self._cluster=set()
        self._edge=defaultdict(list)
        self._nodes=[]

        with open(graph_file,'r') as f:
            self._nodes_num=int(f.readline())
            print self._nodes_num
            for line in f:
             from_vertex,to_vertex,weight=line.split()
                #print from_vertex,to_vertex
             self._edge[int(weight)].append((int(from_vertex),int(to_vertex)))


    def cluster(self,k):
      num = 0
      nodes = union_find(self._nodes_num)
      #print nodes.get_clustersize()
      #print nodes.get_root()
      while num!=k:
        sorted_weight=sorted(self._edge)
        minweight=sorted_weight[0]
        p,q=self._edge[minweight][0]
        print p,q
        nodes.union(p,q)
        #print nodes.get_root()
        #print nodes.get_clustersize()
        if len(self._edge[minweight])>1: del self._edge[minweight][0]
        else: del self._edge[minweight]
        print self._edge
        num=nodes.num_cluster()
      minweight=min(self._edge.keys())
      p,q=self._edge[minweight][0]
      while nodes._findroot(p)==nodes._findroot(q):
          if len(self._edge[minweight]) > 1:
              del self._edge[minweight][0]
          else:
              del self._edge[minweight]
              minweight = min(self._edge.keys())
              p, q = self._edge[minweight][0]
      return minweight
if __name__=="__main__":
  cluster=clustering('input_completeRandom_9_32.txt')
  maxspace=cluster.cluster(4)
  print maxspace