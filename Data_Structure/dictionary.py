dict1 = {1: "HNDIT", 2: "Civil" , 3: "QS"}
print(dict1)
# adding elemet
dict1[4] = "Access"
print(dict1)
# removing element
a = dict1.pop(1)
print(a)
# removing last element
b = dict1.popitem()
print(b)
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())