class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        # add together position and speed, pair in array
        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        # sort big to small
        # start from car that closet to destination(position)
        pair.sort(reverse=True)

        fleets = 1

        # prev = previous car processed in the loop
        # mean closest car to destination
        prevPosition = pair[0][0]
        prevSpeed = pair[0][1]
        # time for the fleet in front(closest to destination) to reach destination
        prevTime = (target - prevPosition) / prevSpeed


        for i in range(1, len(pair)):
            # current car speed and position
            currPosition = pair[i][0] 
            currSpeed = pair[i][1]
            # time for current car(loop move from closest to destination to farthest)
            currTime = (target - currPosition) / currSpeed

            # if current car takes longer than the fleet in front,
            # it cannot catch up, so it forms a new fleet
            if currTime > prevTime:
                fleets += 1
                # current car becomes the new front fleet
                prevTime = currTime
        return fleets