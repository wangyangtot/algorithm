import random
f = open('intergerArrayForInversion.txt', 'r')
x = f.readlines() #python's file.readLines() method returns a list of the lines in the file:
int_array=[]
for i in range(len(x)):
    int_array.append(int(x[i].strip('\n').strip('\r')))
    '''str.strip() returns a string with leading+trailing
     whitespace removed, .lstrip and .rstrip for only leading and trailing respectively.'''

def merge_count(left,right):
    m=len(left)
    n=len(right)
    sorted_array=[]
    count_inversion=i=j=new=0
    while (i<m and j<n):
        # use & is wrong since bitwise & has a higher precedence
        # than "==" (since you wouldn't want expressions like "a & 0xff == ch" to mean "a & (0xff == ch)")
        if left[i]<right[j]:

            sorted_array.append(left[i])
            new=new+1
            i=i+1

        else:
            count_inversion+=(m-i)   #count the remaining # in left
            sorted_array.append(right[j])
            j=j+1
            new=new+1

    if i==m:
        sorted_array[new:m+n]=right[j:n]
    if j==n:
        sorted_array[new:m+n]=left[i:m]

    return sorted_array,count_inversion





def split(int_array):
     m=len(int_array)
     if m%2==0:
      left_array=int_array[0:int(m/2)]
      right_array=int_array[int(m/2):m]
     else: # if the array can't be splited evenly, give the left one more element than the right
          left_array=int_array[0:int(m/2)+1]
          right_array=int_array[int(m/2)+1:m]
     return left_array,right_array

def inversion(int_array):
    if len(int_array)>1:#iterate until the list can't be splited to left and right
         left,right=split(int_array)
         sorted_left,cout_left=inversion(left)
         sorted_right,cout_right=inversion(right)
         int_array,cout_leftAndright=merge_count(sorted_left,sorted_right)

         cout=cout_left+cout_right+cout_leftAndright
         #cout all the # of inversion from left,right and merge
    else:cout=0
    return int_array,cout

s,t=inversion(int_array)
print t