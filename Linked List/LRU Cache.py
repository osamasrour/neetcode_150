# LRU Cache: https://neetcode.io/problems/lru-cache/question?list=neetcode150

class Node:
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class Dll:
    def __init__(self):
        self.front = None
        self.last = None
        self.count = 0

    def addFront(self, key, val):
        if self.front == None:
            assert self.last == None and self.count == 0
            node = Node(key, val)
            node.prev = None
            node.next = None
            self.last = self.front = node
            self.count = 1
        else:
            node = Node(key, val)
            self.front.prev = node
            node.next = self.front
            self.front = node
            self.count += 1

    def addLast(self, key, val):
        if self.last == None:
            assert self.front == None and self.count == 0
            node = Node(key, val)
            node.prev = node
            node.next = node
            self.last = self.front = node
            self.count = 1
        else:
            node = Node(key, val)
            self.last.next = node
            node.prev = self.last
            self.last = node
            self.count += 1

    def remove(self, node: Node):
        if not (node and self.count): return
        if self.count == 1 and node == self.front:
            self.front = None
            self.last = None
            self.count -=1
            return
        if self.front == node:
            self.front = self.front.next
            self.front.prev = None
            self.count-=1
        elif node == self.last:
            self.last = self.last.prev
            self.last.next = None
            self.count -= 1
        else:
            curr = self.front.next
            while curr != self.last:
                if node == curr:
                    prev = curr.prev
                    _next = curr.next
                    prev.next = _next
                    _next.prev = prev
                    curr.prev = None
                    curr.next = None
                    self.count-=1
                    break
                else:
                    curr = curr.next


    def pop(self) -> Node:
        if not self.last: return None
        lastNode = self.last
        if self.count == 1:
            self.last = None
            self.front = None
        else:
            self.last = self.last.prev
            self.last.next = None
        self.count -= 1
        return lastNode


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm: dict[int:Node] = dict()
        self.dll = Dll()

    def get(self, key: int) -> int:
        ret = self.hm.get(key, -1)

        if ret != -1:
            node = ret
            self.dll.remove(node)
            self.dll.addFront(key, node.val)
            self.hm[key] = self.dll.front
            ret = ret.val
        return ret

    def put(self, key: int, value: int) -> None:
        if self.hm.get(key) != None:
            self.hm[key].val = value
            return
        if self.dll.count + 1 > self.cap:
            poped = self.dll.pop()
            assert(poped.key in self.hm)
            del self.hm[poped.key]

        assert(self.dll.count < self.cap)
        self.dll.addFront(key, value)
        self.hm[key] = self.dll.front
        assert len(self.hm) == self.dll.count

# ["LRUCache", [2], "put", [1, 10],
  # "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

# [null,null,10,null,null,20,-1]

cache = LRUCache(2)
print(cache.put(1,10) == None)
print(cache.get(1) == 10)
print(cache.put(2,20) == None)
print(cache.put(3,30) == None)
print(cache.get(2) == 20)
print(cache.get(1) == -1)

# ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], 
# "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]

# [null,null,null,1,null,-1,null,-1,3,4]

cache = LRUCache(2)
print(cache.put(1, 1) == None)
print(cache.put(2, 2) == None)
print(cache.get(1) == 1)
print(cache.put(3, 3) == None)
print(cache.get(2) == -1) # should be -1

print(cache.put(4, 4) == None)
print(cache.get(1) == -1)
print(cache.get(3) == 3)
print(cache.get(4) == 4)