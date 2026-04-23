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
        self.last = self.last.prev
        self.last.next = None
        lastNode.prev = None
        lastNode.next = None
        self.count -= 1
        return lastNode


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm: dict[int: Node] = dict()
        self.dll = Dll()


    def get(self, key: int) -> int:
        ret = self.hm.get(key, -1)
        if ret != -1:
            ret = ret.val
        return ret

    def put(self, key: int, value: int) -> None:
        if self.dll.count + 1 > self.cap:
            rm = []
            for k, v in self.hm.items():
                if self.hm[k] == self.dll.last:
                    rm.append(k)

            assert(len(rm) == 1)
            del self.hm[rm[0]]
            self.dll.pop()

        assert(self.dll.count < self.cap)

        self.dll.addFront(value)
        self.hm[key] = self.dll.front

