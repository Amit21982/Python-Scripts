#give a list find pair of sum

def findpairs(list, sum):
    if len(list) <=1:
        return 'Invalid length of list is provided'
    seen = set()
    pair_list= []
    for num in list:
        target = sum - num
        if target not in seen:
            seen.add(num)
        else:
            pair_list.append((min(num, target), max(num, target)))
    return pair_list

#print(findpairs([2,3,4,1,6], 5))
def compressString(s):
    if len(s) == 0 and len(s) ==1:
        return s
    startchar = s[0]
    compressStr = ""
    counter = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            if counter > 1:
                compressStr += s[i-1] + str(counter)
                counter = 1
            else:
                counter = 1
                compressStr += s[i] + str(counter)

        if i == len(s) -1:
            compressStr += s[i-1] + str(counter)

#print(compressStr)
#compressString('AAAABBBCC')

import re
name = 'harish Harsh Harikota america kota'
list1 = name.split(' ')
print(list(filter(lambda x: x[0] in ['H','h'], list1)))

def rev_num(num):
    rev =0
    while num > 0:
        rem = num%10
        rev = rev * 10 + rem
        num = num//10
    return rev


list = ['a', 'b', 'c', 'd', 'e']
#print(list[::2])
#print(list[::-1])

files = ["test.py", "program.c", "sample.pl", "hello.cpp"]
files.sort(key= lambda x: x.split('.')[1])

def generator():
    files = ["test.py", "program.c", "sample.pl", "hello.cpp"]
    for file in files:
        yield file

gen = generator()
print(next(gen))
print(next(gen))


def fibonacci(num):
    if num == 0 or num == 1:
        return num
    return fibonacci(num -1) + fibonacci(num -2)

#print(fibonacci(10))

def finddifferncebetweentwolist(l1, l2):
    diff = []
    for item in l1:
        if item not in l2:
            diff.append(item)

def findcombinations(str):
    out=[]
    if len(str) == 1:
        return str
    if len(str) == 0:
        return [str]

    for i, char in enumerate(str):
        for perm in findcombinations(str[:i] + str[i+1:]):
            out += [char+perm]
    return out

#print(findcombinations('ABC'))

print(filter(lambda x: x%2 == 0, range(10)))

list1 =[13,45,6,8,4,5,6]
print(list1[-2::][0])


import subprocess
proc = subprocess.Popen(['echo', 'i am the child process'], stdout=subprocess.PIPE)

out, error = proc.communicate()
print(out.decode('utf-8'))

#proc = subprocess.Popen(['sleep', '0.3'])
#from time import sleep
#while proc.poll() is None:
    #print('Working')
    #sleep(0.1)
#print('Exit the process')

from Queue import Queue
from threading import Thread
queue = Queue(1)

def consumer():
    print('Consumer thread waiting')
    queue.get()
    print('Consumer thread done')



def producer(num, thread):
    print('producer thread waiting')
    queue.put(1)
    thread.join()
    print('producer thread done')

#thread = Thread(target=consumer)
#thread.start()
#producer(1, thread)

#from concurrent.futures import ThreadPoolExecutor
#import threading
#from time import sleep

#def somedummysleep(counter):
    #while(counter > 0):
        #print('Counter is %d'%(counter))
        #sleep(1)

#with ThreadPoolExecutor(max_workers=3) as executor:
    #executor.submit(somedummysleep, 5)

def binary_search(list, target):
    if len(list) == 0:
        print('Invalid list')

    lower = 0
    upper = len(list)-1
    while lower < upper:
        mid = (lower+upper)//2
        if list[mid] == target:
            return list[mid]
        elif target < list[mid]:
            upper = mid - 1
        else:
            lower = mid + 1

    return None

#print('Binary search')
#print(binary_search([1,2,3,4,5,6], 5))


class Linklist(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        head = self
        while head != None:
            print(head.value)
    def check_circular(self):
        head = self
        next_node = head
        while next_node.next != None:
            next_node = next_node.next
            if next_node == head:
                return 'circular list'
        return 'Non circlular'
l1 = Linklist(1)
l2 = Linklist(2)
l3 = Linklist(3)
l4 = Linklist(4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l1

#print(l1.check_circular())

def sort_list(list1):
    sorted_list = []
    max_elem = list1[0]
    counter = len(list1)
    while counter > 0:
        for item in list1:
            if max_elem <= item and item not in sorted_list:
                print(max_elem)
                sorted_list.append(item)
                max_elem = item
        counter = counter - 1
    print(sorted_list)

l1 = sort_list([1,3,2,4,5])
l1.sort()
print(l1)
