list1 = [1,2,3,4,8,6]
print(list1[True::1])
print(list1[::-1])
print(list1[2:5])
print(list1[1:4])
print(list1[1:4:2])
print(list1[-5:-2:])
print(sorted(list1)[::-1])

def odd_even(arg):
    if arg %2 == 0:
        return "Even"
    else:
        return "odd"
def sum(a, b):
    return a+b

list1 = [12,18,33,1,7]
op = map(odd_even, list1)
print(list(op))

print(list(filter(lambda i: i%2 ==0, list1)))
#print(reduce(sum, list1))
