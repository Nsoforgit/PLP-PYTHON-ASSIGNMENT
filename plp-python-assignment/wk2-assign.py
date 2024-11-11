#list operations

my_list = []
print("Empty list:", my_list)

my_list.extend([10, 20, 30, 40])
print("After appending elements:", my_list)

my_list.insert(1, 15)
print("After inserting 15 at position 2:", my_list)

my_list.extend([50, 60, 70])
print("After extending the list:", my_list)

my_list.pop()
print("After removing last element:", my_list)

my_list.sort()
print("After sorting:", my_list)

index_30 = my_list.index(30)
print("Index of value 30:", index_30)