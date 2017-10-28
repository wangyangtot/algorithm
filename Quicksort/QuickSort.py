import random
import math
import numpy as np
'''
 def read():
 f = open('filename', 'r')
 x = f.readlines() #python's file.readLines() method returns a list of the lines in the file:
 int_array=[]
 for i in range(len(x)):
    int_array.append(int(x[i].strip('\n').strip('\r')))
'''
     #return int_array
f = open('QuickSortArray.txt', 'r')
x = f.readlines() #python's file.readLines() method returns a list of the lines in the file:
int_array=[]
for i in range(len(x)):
    int_array.append(int(x[i].strip('\n').strip('\r')))
#print(len(int_array))

'''def find_pivot(rarray):
    return 0
'''
def swap(a, b):
      tem = a
      a = b
      b = tem
      return a, b
def median_of_three(rarray):
    m=len(rarray)
    first=0
    last=m-1
    middle=(m-1)/2
    s=[rarray[first],rarray[middle],rarray[last]]
    c=np.median(s)

    if c==rarray[first]: return first
    elif c==rarray[middle]: return middle
    else:return last

def partition(rarray):
      m = len(rarray)
      piv=m-1  #the position of pivot
      rarray[piv], rarray[0] = swap(rarray[piv], rarray[0]) #swap the pivot and first element
      i = j = 1
      while j < m:
          if rarray[j] < rarray[0]:
              rarray[i], rarray[j] = swap(rarray[i], rarray[j])
              i = i + 1
          j = j + 1
          # print rarray
      rarray[0], rarray[i - 1] = swap(rarray[0], rarray[i - 1])
      return rarray,i-1
def QuickSort(rarray):
   m = len(rarray)
   #print rarray
   if m>1:
    rarray,pos=partition(rarray)
    cout=m-1
    left=rarray[0:pos]
    right=rarray[pos+1:m] # be careful!exclude the pivot
    rarray[0:pos],left_cout=QuickSort(left)
    rarray[pos+1:m],right_cout=QuickSort(right)
    cout+=left_cout+right_cout

   else:
       cout=0
   #print rarray,cout

   return rarray,cout
b,c = QuickSort(int_array)
print c

