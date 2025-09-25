#1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#4
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#5
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#6
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#7
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)


#8
thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)

#9
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)

#10
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 

#11
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#12
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#13
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


#14
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


#15
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

