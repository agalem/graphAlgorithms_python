class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def remove(self, element):
        self.items.remove(element)
        return element

    def get_items(self):
        return self.items

    def get_size(self):
        return len(self.items)

    def last_element(self):
        return self.items[-1]