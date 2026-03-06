# Car Fleet: https://neetcode.io/problems/car-fleet/question?list=neetcode150
# TODO: Continue
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
                vdx: int # Virtual distance
                vdx = sx * dy / sy
                vdy = sy * dx / sx
                print("dx = ", dx, ",tx = ", tx, ",sx = ", sx, ",dy = ", dy, ",ty = ", ty, ",sy = ", sy, ",vdx = ", vdx)
                if vdx <= dx and vdx + px == dy + py and vdy + py == dx + px:
                    found_fleet = True
                    fleets[j].append(i)
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