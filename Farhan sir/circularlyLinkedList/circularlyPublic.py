class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularlyLinkedList:
    def __init__(self):
        self.tail = None  
        self.size_count = 0

    def size(self):
        return self.size_count

    def isEmpty(self):
        return self.size_count == 0

    def first(self):
        if self.isEmpty():
            return None
        return self.tail.next.data  # Accessing directly

    def last(self):
        if self.isEmpty():
            return None
        return self.tail.data  # Accessing directly

    def addFirst(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.tail = new_node
            self.tail.next = new_node  # Circular reference to itself
        else:
            new_node.next = self.tail.next  # New node points to head
            self.tail.next = new_node  # Tail points to new head
        self.size_count += 1

    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.tail = new_node
            self.tail.next = new_node  # Circular reference to itself
        else:
            new_node.next = self.tail.next  # New node points to current head
            self.tail.next = new_node  # Tail points to the new node
            self.tail = new_node  # Update tail to be the new node
        self.size_count += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        removed_data = self.tail.next.data  # Access data directly
        if self.size_count == 1:  # If only one element
            self.tail = None
        else:
            self.tail.next = self.tail.next.next  # Tail points to the next head
        self.size_count -= 1
        return removed_data

    def rotate(self):
        if self.size_count > 0:
            self.tail = self.tail.next  # Rotate by moving tail to the next node

    def showList(self):
        if self.isEmpty():
            print("List is empty")
            return
        current = self.tail.next  # Start from head
        while True:
            print(current.data, end=" -> ")  # Access data directly
            current = current.next
            if current == self.tail.next:  # Stop when we circle back to head
                break
        print("... circular")


if __name__ == "__main__":
    list = CircularlyLinkedList()
