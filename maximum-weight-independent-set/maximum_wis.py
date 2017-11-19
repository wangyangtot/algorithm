class max_wis:
    def __init__(self,graph_file):
        self.weight=[]

        with open(graph_file)as f:
          self.num_vertex=int(f.readline())
          self.max_weight=[None]*self.num_vertex
          self.max_vertex_set = [None]*self.num_vertex

          for line in f:
              self.weight.append(int(line.strip()))
          print self.num_vertex

    def max_indep_growth(self):
        self.max_weight[0]=self.weight[0]
        self.max_weight[1]=self.weight[1]
        self.max_vertex_set[0]=[0]
        self.max_vertex_set[1]=[1]
        for i in range(2,self.num_vertex):
            if self.max_weight[i-2]+self.weight[i]>self.max_weight[i-1]:
             self.max_weight[i]=self.max_weight[i-2]+self.weight[i]
             self.max_vertex_set[i]=self.max_vertex_set[i-2]+[i]
            else:
                self.max_weight[i]=self.max_weight[i-1]
                self.max_vertex_set[i]=self.max_vertex_set[i-1]
        #print self.max_vertex_set[999]

    def check_in_max_set(self,check_list):
        binary_list=[]
        for i in check_list:
            if i-1 in self.max_vertex_set[self.num_vertex-1]:
              binary_list.append(1)
            else:binary_list.append(0)
        bi= int(''.join(map(str,binary_list)))
        print bi




a=max_wis('mwis.txt')
a.max_indep_growth()
hw=[1, 2, 3, 4, 17, 117, 517, 997]
a.check_in_max_set(hw)
#answer is 10100110