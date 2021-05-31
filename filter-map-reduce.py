
#find all the names of fruits starting with A


ListofFruits = ['apple', 'Banana', 'Orange']
print(list(map(lambda x: x[0].lower() == 'a', ListofFruits)))
print(list(filter(lambda x: x[0].lower() == 'a', ListofFruits)))
num= list(range(10))
print(list(filter(lambda x: x%2==0,num)))

from functools import reduce
addlambda = lambda x,y: x+y
print(reduce(addlambda, list(range(10))))

import os
fwh = open('temp.txt','w')
counter = 10
while counter > 0:
    fwh.write("Counter value is  - %d " %(counter))
    counter -=1
fwh.close()

frh = open('temp.txt','r')
list1 = frh.readlines()
print list1[::-1]
