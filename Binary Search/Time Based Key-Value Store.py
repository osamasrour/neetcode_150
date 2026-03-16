# Time Based Key-Value Store: https://neetcode.io/problems/time-based-key-value-store/question?list=neetcode150
from inspect import currentframe

def lineno():
    """Returns the current line number in our program."""
    # currentframe() gets the current frame object
    # f_back gets the frame object of the caller
    # f_lineno gets the line number from the frame object
    return currentframe().f_back.f_lineno

class TimeMapValue:
    def __init__(pair, value, timestamp):
        pair.value = value
        pair.timestamp = timestamp
        pair.left: TimeMapValue = None
        pair.right: TimeMapValue = None


class TimeMap:

    def __init__(self):
        self.hashKeys: dict[str, TimeMapValue] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        root = self.hashKeys.get(key)
        if root != None: # the key is in the hashmap
            current_pair = root
            while True:
                if current_pair == None:
                    current_pair = TimeMapValue(value, timestamp)
                    break
                if current_pair.timestamp > timestamp:
                    if current_pair.left == None:
                        current_pair.left = TimeMapValue(value, timestamp)
                        break
                    else:
                        current_pair = current_pair.left
                elif current_pair.timestamp < timestamp:
                    if current_pair.right == None:
                        current_pair.right = TimeMapValue(value, timestamp)
                        break
                    else:
                        current_pair = current_pair.right
                else:
                    current_pair.value == value
                    break
        else: # the key is not in the hashmap
            self.hashKeys[key] = TimeMapValue(value, timestamp)


    def get(self, key: str, timestamp: int) -> str:
        #print(f"[line]:{lineno()} [info] target timestamp = {timestamp}")
        root = self.hashKeys.get(key)
        if root == None:
            return ""
        current_pair = root
        prev_pair = current_pair
        while True:
            if current_pair == None:
                value = prev_pair.value if prev_pair.timestamp <= timestamp else ""
                #print(f"[line]:{lineno()} [info] prev_pair.value = {value}")
                return value
            if current_pair.timestamp > timestamp:
                prev_pair = current_pair
                current_pair = current_pair.left
            elif current_pair.timestamp < timestamp:
                prev_pair = current_pair
                current_pair = current_pair.right
            else:
                #print(f"[line]:{lineno()} [info] current_pair.value = {current_pair.value}")
                return current_pair.value
        #print(f"[line]:{lineno()} [info] current_pair.value ={current_pair.value}")
        return current_pair.value


timeMap = TimeMap();
print(timeMap.set("alice", "happy", 1) == None)    # store the key "alice" and value "happy" along with timestamp = 1.
print(timeMap.get("alice", 1) == "happy")         # return "happy"
print(timeMap.get("alice", 2) == "happy")          # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
print(timeMap.set("alice", "sad", 3) == None)    # store the key "alice" and value "sad" along with timestamp = 3.
print(timeMap.get("alice", 3) == "sad")           # return "sad"

["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]
print("=="*25)
timeMap = TimeMap()
print(timeMap.set("key1", "value1", 10) == None)
print(timeMap.get("key1", 1) == "")
print(timeMap.get("key1", 10) == "value1")
print(timeMap.get("key1", 11) == "value1")
