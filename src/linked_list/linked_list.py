class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def size(self):
        if self.head:
            current = self.head
            count = 1

            while current.next:
                count += 1
                current = current.next

            return count

        return 0

    def get(self, position):
        if self.head and position >= 0:
            current_position = 0
            current = self.head

            if current_position == position:
                return current
            else:
                while current.next:
                    current_position += 1
                    current = current.next

                    if current_position == position:
                        return current

        return None

    def empty(self, position):
        if self.head and position >= 0:
            current_position = 0
            current = self.head

            if current_position == position:
                self.head = None
            else:
                while current.next:
                    current_position += 1
                    
                    if current_position == position:
                        current.next = None
                        break
                    current = current.next

    def append(self, element):
        if self.head:
            current = self.head

            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element

    def rotate(self, number_of_places):
        number_of_places_to_move = self.size() - number_of_places
        node_to_front = self.get(number_of_places_to_move)
        self.empty(number_of_places_to_move)
        node_to_back = self.get(0)
        self.head = node_to_front
        self.append(node_to_back)

    def to_list(self):
        l = []

        if self.head:
            current = self.head
            l.append(current.value)

            while current.next:
                current = current.next
                l.append(current.value)

            return l

        return l

    def __str__(self):
        return str(self.to_list())

if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    node_4.next = node_5
    node_3.next = node_4
    node_2.next = node_3
    node_1.next = node_2
    linked_list = LinkedList(node_1)

    print(linked_list.size())
    print(linked_list.get(3))
    print(linked_list)
    linked_list.rotate(2)
    print(linked_list)