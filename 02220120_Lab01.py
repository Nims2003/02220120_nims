class CustomList:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
        self.items = [] 
        print(f"Created new CustomList with capacity: {self.capacity}")
        print(f"Current size: {self.size}")

    def append(self, element):
        if self.size < self.capacity:
            self.items.append(element)
            self.size += 1
            print(f"Appended {element} to the list")
        else:
            print(f"Cannot append {element}: List is at full capacity")

    def get(self, index):
        return self.items[index] if 0 <= index < len(self.items) else "Index out of range"

    def set(self, index, element):
        if 0 <= index < len(self.items):
            self.items[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of range")

    def list_size(self):
        print(f"Current size: {len(self.items)}")

custom_list = CustomList(5)  
custom_list.append(5)
custom_list.append(10)
print(f"Element at index 0: {custom_list.get(0)}")
custom_list.set(0, 15)
print(f"Element at index 0: {custom_list.get(0)}")
custom_list.list_size()
