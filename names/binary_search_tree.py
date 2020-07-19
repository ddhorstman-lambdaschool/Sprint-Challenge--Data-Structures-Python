class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)
    # Insert the given value into the tree

    def insert(self, value):
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
        return value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target and self.left:
            return self.left.contains(target)
        elif self.value < target and self.right:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        return fn(self.value)

        # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        self = node or self
        if self.left:
            self.left.in_order_print()
        print(self)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        nodes = Queue()
        nodes.enqueue(node)
        while len(nodes) > 0:
            current = nodes.dequeue()
            print(current)
            if current.left:
                nodes.enqueue(current.left)
            if current.right:
                nodes.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node=None):
        self = node or self
        print(self)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node=None):
        self = node or self
        print(self)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):
        self = node or self
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.get_next()
        return length

    def add_to_tail(self, value):
        new_node = Node(value)
        # If list is empty, new entry will be both head and tail
        if self.head is None:
            self.head = self.tail = new_node
        # If list isn't empty, append new entry to previous tail
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        current_head = self.head

        # Empty list
        if current_head is None:
            return None
        # Single-entry list
        elif current_head is self.tail:
            self.head = self.tail = None
        # Multiple-entry list
        else:
            self.head = current_head.get_next()

        return current_head.get_value()

    def remove_tail(self):
        current_tail = self.tail

        # Empty list
        if current_tail is None:
            return None
        # Single-entry list
        elif current_tail is self.head:
            self.head = self.tail = None
            return current_tail.get_value()
        # Multiple-entry list
        else:
            current_node = self.head
            while current_node.get_next() is not self.tail:
                current_node = current_node.get_next()
            self.tail = current_node
            current_node.set_next(None)

            return current_tail.get_value()

    def contains(self, value):
        current_node = self.head

        while current_node:
            if current_node.get_value() is value:
                return True
            current_node = current_node.get_next()
        else:
            return False

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()
        current_node = self.head.get_next()

        while current_node:
            current_value = current_node.get_value()
            if current_value > max_value:
                max_value = current_value
            current_node = current_node.get_next()
        return max_value


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size is 0:
            return None
        self.size -= 1
        return self.storage.remove_head()


