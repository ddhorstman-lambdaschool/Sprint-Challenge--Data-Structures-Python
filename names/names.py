import time
from binary_search_tree import BSTNode
start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure


with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")
    names_1_tree = BSTNode(names_1.pop(0))
    for name in names_1:
        names_1_tree.insert(name)

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")
    for name in names_2:
        if names_1_tree.contains(name):
            duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
