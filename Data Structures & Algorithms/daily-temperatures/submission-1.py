class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # output array, same length as temperatures
        reslt = [0] * len(temperatures)

        # stack stores (temperature, index)
        stack = []

        for i in range(len(temperatures)):
            # current temperature
            t = temperatures[i]

            while len(stack) > 0:
                # temperature at top of stack
                prevTemp = stack[-1][0]

                # stop if current temp isn't warmer
                if t <= prevTemp:
                    break

                # remove top of stack
                poppedItem = stack.pop()

                stackTemp = poppedItem[0]
                stackIndex = poppedItem[1]

                # days until warmer
                reslt[stackIndex] = i - stackIndex

            # add current temperature and index
            stack.append((t, i))

        return reslt