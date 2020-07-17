import time
from binary_search_tree import BSTNode
start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure

# Starter code has a complexity of O(n) * O(n).
# If the lists have the same length, that becomes O(n^2)

# Original solution: BST (74 ms)
# with open('names_1.txt', 'r') as f:
#     names_1 = f.read().split("\n")
#     names_1_tree = BSTNode(names_1.pop(0))
#     for name in names_1:
#         names_1_tree.insert(name)

# with open('names_2.txt', 'r') as f:
#     names_2 = f.read().split("\n")
#     for name in names_2:
#         if names_1_tree.contains(name):
#             duplicates.append(name)

# Fastest solution: sets (3 ms)
# with open('names_1.txt', 'r') as f:
#     names_1 = set(f.read().split("\n"))
# with open('names_2.txt', 'r') as f:
#     names_2 = set(f.read().split("\n"))
# duplicates = names_1 & names_2

# List-only solution using built-in methods: (680 ms)
# with open('names_1.txt', 'r') as f:
#     names_1 = f.read().split("\n")
# with open('names_2.txt', 'r') as f:
#     names_2 = f.read().split("\n")
#     duplicates = [n for n in names_2 if n in names_1]

# Custom list-only solution: (340 ms)
def midpoint_search(needle, haystack):
    if len(haystack) < 2:
        return False
    mid = len(haystack)//2
    if haystack[mid] < needle:
        return midpoint_search(needle, haystack[mid:])
    elif haystack[mid] > needle:
        return midpoint_search(needle, haystack[:mid])
    else:
        return True

with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")
    names_1.sort()
with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")
    duplicates = [n for n in names_2 if midpoint_search(n, names_1)]




end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
