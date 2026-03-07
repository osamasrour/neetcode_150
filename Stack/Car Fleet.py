# Car Fleet: https://neetcode.io/problems/car-fleet/question?list=neetcode150

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        distances: list[int] = []
        for i in position:
        	distances.append(target - i)
            
        times: list[float] = []
        for i in range(n):
           times.append(distances[i] / speed[i])

        fleets: list[list[int]] = []
        fleets.append([])
        fleets[0].append(0)
        for i in range(1, n):
            found_fleet = False
            for j in range(len(fleets)):
                dx = distances[i]
                px = position[i]
                tx = times[i]
                sx = speed[i]
                dy = distances[fleets[j][0]]
                py = position[fleets[j][0]]
                ty = times[fleets[j][0]]
                sy = speed[fleets[j][0]]

                # handle the zero divesion
                if sx == sy:
                    if px == py:
                        found_fleet = True 
                        fleets[j].append(i)
                        if times[fleets[j][-1]] > times[fleets[j][0]]:
                            fleets[j][0], fleets[j][-1] =  fleets[j][-1], fleets[j][0]
                        break
                    else:
                        break

                meet_time = abs(px- py) / (abs(sx- sy))
                if meet_time <= min(tx, ty) and (px + (meet_time * sx)) == (py + (meet_time * sy)):
                    found_fleet = True 
                    fleets[j].append(i)
                    if times[fleets[j][-1]] > times[fleets[j][0]]:
                        fleets[j][0], fleets[j][-1] =  fleets[j][-1], fleets[j][0]
                    break
            if not found_fleet:
                fleets.append([])
                fleets[-1].append(i)
            print(fleets)
        return len(fleets)



# x s3 d9 t3
# y s2 d6 t3

# t = d/s

# ty = tx = dy / 2 = dx / 3 = ?
# dy = 2 * dx / 3 = 2 * 9 / 3 = 6
# dy  <= d6 -> fleet

obj = Solution()
target = 10
position = [1,4]
speed = [3,2]
print(obj.carFleet(target, position, speed) == 1)
print("=" * 25)
target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
print(obj.carFleet(target, position, speed) == 3)
print("=" * 25)

target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
print(obj.carFleet(target, position, speed) == 3)
print("=" * 25)


# TODO: It fails in the third test case.
target=12
position=[4,0,5,3,1,2]
speed=[6,10,9,6,7,2]
print(obj.carFleet(target, position, speed) == 4)
print("=" * 25)