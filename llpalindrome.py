class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        newNode = Node(data)
        temp = self.head

        if self.head is None:
            self.head = newNode

        else:
            while temp.next != None:
                temp = temp.next

            temp.next = newNode

    def printList(self):
        temp = self.head
        print(temp.data)
        while temp.next != None:
            temp = temp.next
            print(temp.data)

    def find_palindrome(self):
        temp = self.head
        arr = []

        while temp.next != None:
            arr.append(temp.data)
            temp = temp.next

        arr.append(temp.data)

        rev_arry = reversed(arr)

        if ''.join([str(x) for x in arr]) == ''.join([str(x) for x in rev_arry]):
            print("PALINDROME")
        else:
            print("NOT A PALINDROME")


ll = LinkedList()

ll.add_node(1)
ll.add_node(2)
ll.add_node(2)
ll.add_node(3)

ll.printList()
ll.find_palindrome()



