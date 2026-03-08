# Car Fleet: https://neetcode.io/problems/car-fleet/question?list=neetcode150
# TODO: This solution couldn't be the most optimal solution to this problem. Look at the others who solved it better.
class Car:
    def __init__(self, start, dist, speed):
        self.pos  = start
        self.dist = dist
        self.speed = speed
        self.time = self.dist / self.speed

    def __str__(self): # for debugging purpose only.
        return f"Car <pos: {self.pos}, dist: {self.dist}, speed: {self.speed}, time: {self.time}>"

class Fleet(list):
    def __init__(self):
        self.members: list[Car] = []
        self.time = -1 # means uninitialized

    def append(self, member: Car):
        self.members.append(member)
        self.time = max(self.time, member.time)

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        cars: list[Car] = []
        for i in range(n):
            car = Car(position[i], target - position[i], speed[i])
            cars.append(car)
        
        cars = sorted(cars, key=lambda x: x.pos, reverse=True)
        fleets: list[Fleet] = []
        for car in cars:
            if len(fleets) == 0:
                fleets.append(Fleet())
                fleets[0].append(car)
                continue;
            found_fleet: bool = False
            for fleet in fleets:
                if car.time <= fleet.time:
                    fleet.append(car)
                    found_fleet = True
                    break

            if not found_fleet:
                fleets.append(Fleet())
                fleets[-1].append(car)
        return len(fleets)

