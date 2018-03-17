class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False

        while current:
            if current.data == data:
                if current == self.head:
                    self.head.next.prev = None
                    self.head = current.next
                elif current == self.tail:
                    self.tail.prev.next = None
                    self.tail = current.prev
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                node_deleted = True
            current = current.next

        if node_deleted:
            self.count -= 1

    def contains(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def size(self):
        return self.count

class CircularLinkedList(DoublyLinkedList):
    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.next = self.head
            node.prev = self.tail
            self.tail = node

        self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False

        while current:
            if current.data == data:
                if current == self.head:
                    self.head.next.prev = self.tail
                    self.head = current.next
                    self.tail.next = self.head
                elif current == self.tail:
                    self.tail.prev.next = self.head
                    self.tail = current.prev
                    self.head.prev = self.tail
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                node_deleted = True
            current = current.next

        if node_deleted: self.count -= 1

friends = CircularLinkedList()
friends.append('john')
friends.append('luke')
friends.append('brian')

#for friend in friends.iter():
#    print(friend)