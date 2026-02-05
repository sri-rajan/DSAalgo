# Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add(self, a, b):
        return a + b

    # delete
    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp.data == None:
            return
        prev.next = temp.next

    # length
    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print(count)

    # serch
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("True")
                return
            temp = temp.next
        print("False")
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")


lnk1 = LinkedList()
print("INITIATED :")
lnk1.display()
lnk1.append(3)
lnk1.append(4)
lnk1.append(5)
print("after appending 3,4,5 :")
lnk1.display()
lnk1.prepend(2)
lnk1.prepend(1)
print("after prepending 2,1 :")
lnk1.display()
lnk1.delete(3)
lnk1.delete(4)
lnk1.delete(5)
print("after delete 3, 4, 5 :")
lnk1.display()
lnk1.append(3)
lnk1.append(4)
lnk1.append(5)
print("after appending 3,4,5 :")
lnk1.display()
print("Total Count :")
lnk1.length()
print("searching 2")
lnk1.search(2)
print("searching 15")
lnk1.search(15)
