
hashint={}
with open('2-sum.txt')as f:
    for line in f:
     line=int(line.rstrip('\n'))
     hashint[line]=True

def hash_search(hashint,t):
    for i in hashint:
        j=t-i
        #print j
        if (j in hashint) and (i!=j):
          print (i,j)
          return (i,j)


def cout(hashint):
     cout=0
     for t in range(-10000,10001):
         if hash_search(hashint,t):
             cout+=1
     return cout
c=cout(hashint)
print c


answer is 427