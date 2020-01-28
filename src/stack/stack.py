class Element:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head

        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

class Stack:

    def __init__(self, top=None):
        self.linked_list = LinkedList(top)

    def push(self, new_element):
        self.linked_list.insert_first(new_element)

    def pop(self):
        self.linked_list.delete_first()

if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)

    s = Stack(e1)

    s.push(e2)
    print(s.pop().value)