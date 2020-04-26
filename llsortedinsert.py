class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def sortedInsert(self, newNode):

        if self.head is None:
            newNode.next = self.head
            self.head = newNode

        elif self.head.data >= newNode.data:
            newNode.next = self.head
            self.head = newNode

        else:
            current = self.head
            while current.next is not None and current.next.data < newNode.data:
                current = current.next

            newNode.next = current.next
            current.next = newNode


llist = LinkedList()
new_node = Node(5)
llist.sortedInsert(new_node)
new_node = Node(10)
llist.sortedInsert(new_node)
new_node = Node(7)
llist.sortedInsert(new_node)
new_node = Node(3)
llist.sortedInsert(new_node)
new_node = Node(1)
llist.sortedInsert(new_node)
new_node = Node(9)
llist.sortedInsert(new_node)
print("Create Linked List")
llist.printList()