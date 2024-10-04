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
            self.tail = None 
        self.size_count -= 1
        return removed_data

    def showList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def addAtPosition(self, data, position):
        if position < 0 or position > self.size_count:
            raise IndexError("Invalid position")
        new_node = Node(data)
        if position == 0:
            self.addFirst(data)
        elif position == self.size_count:
            self.addLast(data)
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size_count += 1
    
    def deleteAtPosition(self, position):
        if self.isEmpty():
            return None
        if position < 0 or position >= self.size_count:
            raise IndexError("Invalid position")
        if position == 0:
            return self.removeFirst()
        current = self.head
        for _ in range(position - 1):
            current = current.next
        removed_data = current.next.data
        current.next = current.next.next
        if current.next is None:  
            self.tail = current
        self.size_count -= 1
        return removed_data

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    
    def bubbleSort(self):
        if self.size_count <= 1:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def swapNodes(self, data1, data2):
        if data1 == data2:
            return
        prev1 = prev2 = None
        node1 = node2 = self.head
        while node1 and node1.data != data1:
            prev1 = node1
            node1 = node1.next
        while node2 and node2.data != data2:
            prev2 = node2
            node2 = node2.next
        if not node1 or not node2:
            return
        if prev1:
            prev1.next = node2
        else:
            self.head = node2
        if prev2:
            prev2.next = node1
        else:
            self.head = node1
        node1.next, node2.next = node2.next, node1.next
    

if __name__ == "__main__":
    l1 = SinglyLinkedList()
    