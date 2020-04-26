class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def push(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_node


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next


    def deleteNode(self, data):
        temp = self.head


        if temp.data == data:

            if temp.next is not None:
                temp.data = temp.next.data
                temp.next = temp.next.next
            else:
                print('list cant be made empty')

            return

        while temp.next is not None and temp.next.data != data:
            temp = temp.next


        if temp.next is None:
            print('Node is not present')
        else:
            temp.next = temp.next.next