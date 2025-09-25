#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
myset = {"apple", "banana", "cherry"}

print(type(myset))


#3
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#4
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#5
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#6
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#7
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


#8
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#9
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#10
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

