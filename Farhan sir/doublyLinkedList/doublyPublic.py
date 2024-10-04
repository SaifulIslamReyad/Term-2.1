class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_count = 0

    def size(self):
        return self.size_count

    def isEmpty(self):
        return self.size_count == 0
    def first(self):
        if self.isEmpty():
            return None  # Return None if the list is empty
        return self.head.data  # Return the data of the first node
    # Method to get the last element (tail)
    def last(self):
        if self.isEmpty():
            return None  # Return None if the list is empty
        return self.tail.data  # Return the data of the last node
    
    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node  # The list is empty, so new node is both head and tail
        else:
            new_node.next = self.head  # The new node points to the current head
            self.head.prev = new_node  # The current head's previous pointer points to the new node
            self.head = new_node  # Update the head to the new node
        self.size_count += 1

    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node  # The list is empty, so new node is both head and tail
        else:
            self.tail.next = new_node  # The current tail's next pointer points to the new node
            new_node.prev = self.tail  # The new node's previous pointer points to the current tail
            self.tail = new_node  # Update the tail to the new node
        self.size_count += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        removed_data = self.head.data
        if self.head == self.tail:  # Only one element in the list
            self.head = self.tail = None
        else:
            self.head = self.head.next  # Move head to the next node
            self.head.prev = None  # Set the previous pointer of the new head to None
        self.size_count -= 1
        return removed_data

    def removeLast(self):
        if self.isEmpty():
            return None
        removed_data = self.tail.data
        if self.head == self.tail:  # Only one element in the list
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev  # Move tail to the previous node
            self.tail.next = None  # Set the next pointer of the new tail to None
        self.size_count -= 1
        return removed_data

    def showListForward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def showListBackward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
