INITIAL_CAPACITY = (26+26+10+2)**4

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        if type(key) is str:
            p = 1
            for idx, c in enumerate(key):
                hashsum += (ord(c) - ord('a')) * p

                hashsum = hashsum % self.capacity
                p *= 31
        elif type(key) is int:
            hashsum = key % self.capacity
        return hashsum

    def getAll(self):
        to_ret = []
        for i, node in enumerate(self.buckets):
            if node is not None:
                newn = node
                p = 0
                while newn is not None:
                    to_ret.append((str(i) + f' + {p}', newn.key, newn.value))
                    newn = newn.next
                    p+=1

        return to_ret

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)

    def find(self, key):

        index = self.hash(key)

        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def getIndex(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        collis = 0
        while node is not None and node.key != key:
            collis += 1
            node = node.next

        if node is None:
            return -1
        else:
            return str(index) + f' + {str(collis)}'

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:

            return None
        else:

            self.size -= 1
            result = node.value

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next

            return result
