from __future__ import division
import math
from collections import defaultdict


length=[]
difference=defaultdict(list)
ratio=defaultdict(list)
with open('greedy_job.txt') as f:
    for line in f:
       a,b=line.split(' ')
       data={}
       #print line
       data['weight']=int(a)
       data['length']=int(b)
       index=int(a)-int(b)
       difference[index].append(data)
       tem=int(a)/int(b)
       ratio[tem].append(data)
sorted_key_of_difference=sorted(difference,reverse=True)
sorted_key_of_ratio=sorted(ratio,reverse=True)
#print sorted_key_of_difference
#print difference


def sum_of_weighted_completion_times(sorted_array,dic):
    sum=0
    time=0
    for i in sorted_array:
        weight=defaultdict(list)
        for item in dic[i]:
            weight[item['weight']].append(item['length'])
            #print weight
        sorted_weight=sorted(weight,reverse=True)
        #print sorted_weight
        #print weight
        for k in sorted_weight:
             for j in weight[k]:
              time+=j
              sum+=k*time
              #print time,sum
    return sum,time
a,b=sum_of_weighted_completion_times(sorted_key_of_difference,difference)
c,d=sum_of_weighted_completion_times(sorted_key_of_ratio,ratio)
print a
print c