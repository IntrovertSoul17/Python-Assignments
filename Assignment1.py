
list=[1,2,3,4,5]
print(list)

print(list[2])

list.append(6)
print("list after adding 6:",list)
list.remove(3)
print("list after removing 3 :",list)

list.insert (2,10)
print("list after inserting 10 at index 2:",list)

list.pop()
print("list after popping last elemnt :",list)
 
list.sort()
print("list after sorting in ascending order :",list)

list.sort(reverse=True)
print("list after sorting in descending order:",list)

list.reverse()
print("list after reversing elements:",list)
print("list after sorting in descending order:",list)

list.reverse()
print("list after reversing elements :",list)