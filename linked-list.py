class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')

n1.next = n2
n2.next = n3

#current = n1
#while current:
#    print(current.data)
#    current = current.next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node

        self.size += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                elif current == self.head:
                    self.head = prev
                else:
                    prev.next = current.next
                self.size -= 1
            prev = current
            current = current.next

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def contains(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

words = SinglyLinkedList()

words.append('john')
words.append('luke')
words.append('brian')

words.delete('john')
words.delete('brian')

words.append('connor')
words.append('grant')

for word in words.iter():
    print(word)