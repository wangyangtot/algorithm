import Queue
median= Queue.Queue(maxsize=10000)

with open('median.txt') as f:
    for line in f:
       median.put(int(line))

def init_heap(root):
   tem=[]
   tem.append(root)
   return tem

def swap(p,q):
    tem=q
    q=p
    p=tem
    return p,q

def max_insert(heap,value):
    heap.append(value)
    m=len(heap)
    i=m-1
    #print heap
    while i>0 and heap[i]>heap[(i-1)/2]:
       heap[i],heap[(i-1)/2]=swap(heap[i],heap[(i-1)/2])
       i=(i-1)/2

def min_insert(heap,value):
    heap.append(value)
    m=len(heap)
    i=m-1
    while i>0 and heap[i]<heap[(i-1)/2]:
       heap[i],heap[(i-1)/2]=swap(heap[i],heap[(i-1)/2])
       i=(i-1)/2

def max_del(heap):
    m=len(heap)
    #print heap
    heap[0]=heap[m-1]
    heap.pop(m-1)
    index=0
    #print heap
    while (2*index+2<m-1)and (heap[index]<max(heap[2*index+1],heap[2*index+2])):# vertex has two children
        if heap[2*index+1]<heap[2*index+2]:
            heap[index],heap[2*index+2]=swap(heap[index],heap[2*index+2])
            index=2*index+2
        else:
            heap[index],heap[2*index+1]=swap(heap[index],heap[2*index+1])
            index=2*index+1
    if m-2==index*2+1 and heap[2 * index + 1]>heap[index]:
        heap[index], heap[2 * index + 1] = swap(heap[index], heap[2 * index + 1])
def min_del(heap):
    m = len(heap)
    heap[0] = heap[m - 1]
    heap.pop(m - 1)
    #print heap
    index = 0
    while (2*index+2<m-1) and (heap[index]>min(heap[2 * index + 1], heap[2 * index + 2])):
        if heap[2 * index + 1] >heap[2 * index + 2]:
            heap[index], heap[2 * index + 2] = swap(heap[index], heap[2 * index + 2])
            index=index*2+2
        else:
            heap[index], heap[2 * index + 1] = swap(heap[index], heap[2 * index + 1])
            index=index*2+1
    if m-2==index*2+1 and heap[2 * index + 1]<heap[index]:
        heap[index], heap[2 * index + 1] = swap(heap[index], heap[2 * index + 1])


def banlance(max_heap,min_heap):# if the diffrence between two heaps is over two, adjust number to make it balance
    if len(max_heap)-len(min_heap)==2:
        min_insert(min_heap,max_heap[0])
        max_del(max_heap)
    elif len(min_heap)-len(max_heap)==2:
        max_insert(max_heap,min_heap[0])
        min_del(min_heap)

def median_Maintenance(median):
    min_heap=[]
    val = median.get()
    max_heap=init_heap(val)
    sum=val
    val=median.get()
    if val>max_heap[0]:
        min_heap=init_heap(val)
    else:
        max_insert(max_heap,val)
        tem=max_heap.pop(0)
        min_heap=init_heap(tem)
    sum += max_heap[0]
    i=3
    while median.empty()==False:

      val=median.get()
      if val<max_heap[0]:
            max_insert(max_heap,val)
      else:min_insert(min_heap,val)
      banlance(max_heap,min_heap)

      if len(min_heap)>len(max_heap):
            sum+=min_heap[0]
      else:
            sum+=max_heap[0]
      i=i+1

    return sum

a=median_Maintenance(median)
print a%10000
