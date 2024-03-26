#create empty list
my_list = []

#appending
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting
my_list.insert(1, 15)

# Extending : [50, 60, 70]
my_list.extend([50, 60, 70])

# Removeing the last element from 
my_list.pop()

# Sorting  in ascending order
my_list.sort()

# Finding and printing the index of the value 30 
index_30 = my_list.index(30)

# Print 
print(f"my_list: {my_list}")
print(f"Index of 30: {index_30}")
