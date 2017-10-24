import math
import time
def split(str):
    m=len(str)
    i=0
    t=[]
    while(i<m):
       tem=int(str[i]+str[i+1])
       t.append(tem)
       i=i+2
    return t
def bigmul(p,q):
    i=0
    j=0
    sum=0
    m=len(p)
    n=len(q)
    for i in range (m):
        for j in range(n):
            sum+=(10**(m-2*i+n-2*j))*p[i]*q[j]
            print(sum)
    return sum
#string1="3456"
#string2="4545"
string1='3141592653589793238462643383279502884197169399375105820974944592'
string2='2718281828459045235360287471352662497757247093699959574966967627'
t0=time.time()
array1=split(string1)
array2=split(string2)
product=bigmul(array1,array2)
t1=time.time()
print'time consumes is',t1-t0
#print " ".join('%02d'%x for x in array1)
#print " ".join('%02d'%x for x in array2)
print 'the prduct is ',product


