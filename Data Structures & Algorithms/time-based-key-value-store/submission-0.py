# TIME-BASED KEY VALUE STORE
# set(): save values under a key with their timestamp
# get(): use binary search to find 
# the latest value at or before given timestamp
class TimeMap:

    def __init__(self):
        # list of [val, timestamp]
        self.store = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key does not exist yet, create empty list for it
        if key not in self.store: 
            self.store[key] = []

        # add value and timestamp to that key
        # timestamps are given in increasing order
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        # default answer if key/value cannot be found
        result = ""

        # get all [value, timestamp] pairs for key
        # if key does not exist, use empty list
        values = self.store.get(key, [])

        # binary search
        l = 0
        r = len(values) - 1
        while l <= r: 
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result