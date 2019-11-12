
class Node:

    def __init__(self, next=None, prev=None, data=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def add_node(self, new_data):
        new_node = Node(data=new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, new_data):
        # 1. check if the given prev_node is NULL
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        # 2. allocate node  & 3. put in the data
        new_node = Node(data=new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node


    def add_node_end(self, new_data):
        curr_node = self.head

        while curr_node.next is not None:
            curr_node = curr_node.next

        new_node = Node(data=new_data)

        curr_node.next = new_node
        new_node.next = None
        new_node.prev = curr_node



