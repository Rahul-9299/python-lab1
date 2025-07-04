# Remove elements from a list that are also present in another list
list1 =set( [1, 2, 3, 4, 5, 6, 7])
list2 = set([11,12,13,5,6,4])

result = list1-list2
print("Resulting list:", result)