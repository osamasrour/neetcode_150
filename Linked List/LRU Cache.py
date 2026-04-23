# LRU Cache: https://neetcode.io/problems/lru-cache/question?list=neetcode150

class Node:
    def __init__(self: Node, val: int):
        self.val = val
        self.prev = None
        self.next = None

class Dll:
    def __init__(self):
        self.front = None
        self.last = None
        self.count = 0

    def addFront(self, val):
        if self.front == None:
            assert(self.last == None and self.count == 0)
            node = Node(val)
            node.prev = node
            node.next = node
            self.last = self.front = node
            self.count = 1
        else:
            node = Node(val)
            self.front.prev = node
            node.next = self.front
            self.front = node
            self.count+=1

    def addLast(self, val):
        if self.last == None:
            assert(self.front == None and self.count == 0)
            node = Node(val)
            node.prev = node
            node.next = node
            self.last = self.front = node
            self.count = 1
        else:
            node = Node(val)
            self.last.next = node
            node.prev = self.last
            self.last = node
            self.count+=1

    def pop(self) -> Node:
        lastNode = self.last
        lastNode.prev = None
        lastNode.next = None
        self.last = self.last.prev
        self.last.next = None
        self.count -= 1
        return lastNode



class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass  