# Time Based Key-Value Store: https://neetcode.io/problems/time-based-key-value-store/question?list=neetcode150

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
        root = self.hashKeys.get(key)
        if root == None:
            return ""
        current_pair = root
        prev_pair = current_pair
        while True:
            if current_pair == None:
                value = prev_pair.value if prev_pair.timestamp <= timestamp else ""
                return value
            if current_pair.timestamp > timestamp:
                current_pair = current_pair.left
            elif current_pair.timestamp < timestamp:
                prev_pair = current_pair
                current_pair = current_pair.right
            else:
                return current_pair.value
        return current_pair.value