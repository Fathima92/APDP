list1 =["BCAS", 1,2,3]
#tuple =(1,2,3,4)
# append(),extend(),insert()
print("Adding Elements on the list")
list1.append((2,0)) # add as tuple
list1.extend((2,0)) # add as elemets
list1.insert(3, "HNDIT")

# del, pop, remove
del list1[3]
print(list1)
a = list1.pop(4)
print(a)
list1.remove(2)

# range of list elements
print(list1)
print(list1[0:2])
print(list1[0:4:2])
print(list1[::-1])

# sorting the list
list2 = [1,4,85,549,2,5,6]
print(sorted(list2))
list2.sort(reverse=True)
print(list2)
print(list2.index(2))
print(list2.count(2))

list3 = [1,2,3.4]
list3[2] = 5
print(list3)

list4 = []