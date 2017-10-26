import math
import time
def carry(augent,index,addent):
     sum=augent[index]+addent
     if sum>9:
          augent[index]=int(str(sum)[1])
          if  index==0:
              augent=[0]+augent
              carry(augent,index,1)
          else:carry(augent,index-1,1)
     else:
           augent[index]=sum
     return augent

def enlong(t,index):
    new=[0]*index
    new.extend(t)
    return new

def addone(t,temparameter):
    m=len(t)
    stradd=str(temparameter['value'])
    n=len(stradd)
    start= temparameter['power']
    if m-start-n<0:
        t=enlong(t,start+n-m)
        m=len(t)
    my_list=t[m-start-n:m-start]
    num = int(''.join(map(str, my_list)))
    print my_list
    print 'add term is',num
    print 'value is',temparameter['value']
    tem=num+temparameter['value']
    print'the sum term is',tem
    ltem=map(int, str(tem))
    if tem < 10 ** n:
      t[m - start - n:m - start] = ltem
    else:
         t[m - start - n:m - start] = ltem[1:]
         t=carry(t,m-start-n-1,1)
    print t
    return t

def split(str):
  m=len(str)
  i=0
  list_split=[]#m/2 length
  while (i < m):
    
      tem = int(str[i] + str[i + 1])
      tenpower=m-2-i
      i = i + 2
      parameter={'value':tem,'power':tenpower}
      list_split.append(parameter)
  return list_split

def add_to_product(product,s):
   m=len(s)
   for i in range(m):
      product=addone(product, s[i])
   return product

def Karatsuba(multi1,multi2):
    multi=[]
    m=len(multi1)
    n=len(multi2)
    for i in range(m):
      for j in range(n):
        temvalue=multi1[i]['value']*multi2[j]['value']
        tempower=multi1[i]['power']+multi2[j]['power']
        parameter={'value':temvalue,'power':tempower}
        multi.append(parameter)
    return multi

    
#string1="345634"
#string2="453938"
string1='3141592653589793238462643383279502884197169399375105820974944592'
string2='2718281828459045235360287471352662497757247093699959574966967627'
t0=time.time()
p=[0]
array1=split(string1)
array2=split(string2)
s=Karatsuba(array1,array2)
multiproduct=add_to_product(p,s)
#r=add_to_product(p,s)
#product=add(product,array1)
#product=addarray2)
#product=bigmul(array1,array2)
t1=time.time()
#print'time consumes is',t1-t0
#print r
print(multiproduct)
print "".join('%01d'%x for x in multiproduct)
#print 'the prduct is ',product


