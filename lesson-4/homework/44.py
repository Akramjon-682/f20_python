# # 1. Sort a Dictionary by Value (Ascending and Descending)
# my_dict = {'apple': 10, 'banana': 5, 'cherry': 15}
# # Ascending
# sorted_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# print("Ascending:", sorted_asc)
# # Descending
# sorted_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
# print("Descending:", sorted_desc)

# # 2. Add a Key to a Dictionary
# d = {0: 10, 1: 20}
# d[2] = 30
# print("Updated Dictionary:", d)

# # 3. Concatenate Multiple Dictionaries
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# merged = {}
# for d in (dic1, dic2, dic3):
#     merged.update(d)
# print("Merged Dictionary:", merged)

# 4. Generate a Dictionary with Squares (1 to n)
n = 5
# squares = {x: x*x for x in range(1, n+1)}
# print("Squares Dictionary:", squares)

# # 5. Dictionary of Squares (1 to 15)
# squares_15 = {x: x*x for x in range(1, 16)}
# print("Squares 1 to 15:", squares_15)

# 1. Create a Set
my_set = {1, 2, 3, 4, 5}
# print("Set:", my_set)

# # 2. Iterate Over a Set
# for item in my_set:
#     print(item)

# # # 3. Add Member(s) to a Set
# my_set.add(6)
# my_set.update([7, 8])  # Adding multiple items
# print("Updated Set:", my_set)

# # 4. Remove Item(s) from a Set
# my_set.remove(3)  # Will raise error if not found
# my_set.discard(2) # Will NOT raise error if not found
# print("After Removing:", my_set)

# # 5. Remove an Item if Present in the Set
item_to_remove = 10
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
else:
    print(f"{item_to_remove} not in set")
print("Final Set:", my_set)
