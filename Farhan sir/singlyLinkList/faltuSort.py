class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_count = 0

    def size(self):
        return self.size_count
    
    def isEmpty(self):
        return self.head is None
    
    def first(self):
        if self.isEmpty():
            return None
        return self.head.data
    
    def last(self):
        if self.isEmpty():
            return None
        return self.tail.data
    
    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size_count += 1

    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size_count += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None ###############
        self.size_count -= 1
        return removed_data

    def showList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def faltusort(self):
        current= self.head
        min= current.data
        while current.next:
            if current.next.data>min : current.next= current.next.next
            else: min = current.next.data ; current= current.next
if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.addLast(5)
    l1.addLast(4)
    l1.addLast(9)
    l1.addLast(6)
    l1.addLast(1)
    l1.faltusort()
    l1.showList()
