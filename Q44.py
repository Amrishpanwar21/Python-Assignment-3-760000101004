list1 = [10, 20, 30]

list2 = list1.copy()
list3 = list1

list1.append(40)

print("Original list =", list1)
print("Using copy() =", list2)
print("Using assignment =", list3)