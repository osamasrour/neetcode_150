# Car Fleet: https://neetcode.io/problems/car-fleet/question?list=neetcode150

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ps = [(p, s) for p, s in zip(position, speed)]
        n = len(ps)
        ps = sorted(ps, reverse=True)
        stack = []
        for p, s in ps:
            time: float = (target - p) / s

            if stack and time > stack[-1]:
                stack.append(time)
                continue

            if not stack: stack.append(time)

        return len(stack)