path_to=['7','37','59','82','99','115','133','165','188','197']
edge=[]
edgeweight={}
no_path=1000000
vertexs=[]
with open('Dijkstra\'s.txt','r') as f:
   for line in f:

       tem=line.strip().split('\t')
       #print tem
       dijkstra.append(tem)
       edgeweight[tem[0]]={}
       if tem[0] not in vertexs:
           vertexs.append(tem[0])
       for i in tem[1:]:
         a,b=i.split(',')
         item=(tem[0],a)
         edge.append(item)
         edgeweight[tem[0]][a]=int(b)

def find_min(edgeweight,vertex):
   values=[value for key,value in edgeweight[vertex].items()]
   minvalue=min(values)
   minkeys=[key for key,value in edgeweight[vertex].items() if value==minvalue]
   minkey=minkeys[0]
   return minvalue,minkey


def init_frontier(source,edgeweight,vertexs):
  frontier={}
  for vertex in vertexs:
      if vertex!=source:
       frontier[vertex]=no_path
  for key,value in edgeweight[source].items():
      frontier[key]=value
  return frontier

def update_frontier(vertex,frontier,edgeweight,knownvertex):#update the frontier when vertex is choose to one of the knownvertexs
    knownvertex.append(vertex)
    print knownvertex
    for key,value in edgeweight[vertex].items():
       if key not in knownvertex:
         tem=min(frontier[key],frontier[vertex]+value) #compare the previous frontier with the updating one
         frontier[key]=tem
         print frontier
    return frontier

def find_vertex(frontier,knownvertex): #find the vertex which frontier is minium
    values=[value for key,value in frontier.items() if key not in knownvertex]
    minval=min(values)
    keys=[key for key,value in frontier.items()if (value==minval and key not in knownvertex)]
    minkey=keys[0]
    return minkey,minval


def short_path(source,edgeweight,vertexs):
    frontier=init_frontier(source,edgeweight,vertexs)
    num=len(vertexs)
    knownvertex=[]
    knownvertex.append(source)
    print frontier
    while len(knownvertex)!=num:# if the frontier don't be
          minkey,minval=find_vertex(frontier,knownvertex)
          print minkey,minval
          update_frontier(minkey,frontier,edgeweight,knownvertex)
    return frontier



path_toall=short_path('1',edgeweight,vertexs)
choose_path=[]
for i in path_to:
    choose_path.append(path_toall[i])
print choose_path


