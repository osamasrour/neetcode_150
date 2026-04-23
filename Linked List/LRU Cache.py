# LRU Cache: https://neetcode.io/problems/lru-cache/question?list=neetcode150

from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0
        self.hm: dict[int: int] = dict()
        self.dll: deque = deque()

    def get(self, key: int) -> int:
        value = self.hm.get(key)
        if value == None: return -1

        if self.dll.index(value) != 0:
            self.dll.remove(value)
            self.dll.append(value)
            self.hm[key] = self.dll[0]

        return value

    def put(self, key: int, value: int) -> None:
        if self.count + 1 > self.cap:
            val = self.dll.popleft()
            once = 0
            for k, v in self.hm.items():
                if v == val:
                    del self.hm[k]
                    once+= 1
            assert(once == 1, "should happend only once")

        self.hm[key] = value
        self.dll.append(value)
        self.count+=1


        