class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
        print("Created new LinkedList")
        print("Current size: 0")
        print("Head: None")

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1  # Update size when appending
        print(f"Appended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set(self, index, element):
        current = self.get_node(index)
        current.data = element
        print(f"Set element at index {index} to {element}")

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1  # Fix: Update size when prepending
        print(f"Prepended {element} to the list")

    def get_node(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Print Linked List: [" + " ".join(elements + ["5"]) + "]"


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    print(ll)  # Should print: Print Linked List: [5]

    print(f"Element at index 0: {ll.get(0)}")
    ll.set(0, 10)  # Set the element at index 0 to 10
    print(f"Element at index 0: {ll.get(0)}")

    ll.prepend(10)  # Prepend first 10
    print(ll)  # Should print: Print Linked List: [10 -> 10]
