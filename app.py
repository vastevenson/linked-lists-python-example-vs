'''
Goal: create a linked list class that allows for CRUD (create, read, update, delete) operations
Example linked list: head('a') -> n2('b') -> n3('c') -> None/Null
'''


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        # None is equivalent to Null in Python
        self.next = next_node


class LinkedList:
    def __init__(self):
        # declare nodes and set their data
        self.head = Node(data='a')
        self.n2 = Node(data='b')
        self.n3 = Node(data='c')

        # link the nodes to make the Linked List
        self.head.next = self.n2
        self.n2.next = self.n3
        print(self.count_nodes(self.head))
        print()

    def count_nodes(self, node_obj):
        # assume that we get the head node
        count = 1
        # recursion?
        # base case: node_obj.next == Null
        # recursive case: node_obj.next != Null, get next node and increment counter
        current_node = node_obj
        while current_node.next != None:
            count += 1
            # reference the next node by updating the current node object to reference it's next node
            current_node = current_node.next
        return count


LinkedList()