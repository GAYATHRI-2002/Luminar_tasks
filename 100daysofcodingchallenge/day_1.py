#create a list
list1 = [1,2,3,"apple"]
print(list1)

#conver list to tuple
tuple1 = (1,2,3,3.12,'apple')
print(list(tuple1))
print(type(list(tuple1)))

#add lements in list
a = [3,4,23,11,67,4,'bag']
a.append('ball')
print(a)
things = [1,2,3,'bell']
other_things = ['bat','apple',22,33,43]
things.extend(other_things)
print(things)
fruits = ['apple','orange','banana']
fruits.insert(1,'mango')
print(fruits)

# Python Program to Swap Two Elements in a List
list1 = [22,12,34,32,54]
list1[0],list1[1] = list1[1],list1[0]
print(list1)

list1 = [22,12,34,23]
temp = list1[1]
list1[1] = list1[0]
list1[0] = temp
print(list1)

