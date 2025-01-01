class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Summary: Sort pos and spe array, then calculate time to reach dest
        # then only add times in stack that are in sorted order to capture fleets.
        combined = list(zip(position, speed))
        sort_combined = sorted(combined)
        pos_arr, spe_arr = zip(*sort_combined)
        pos = list(pos_arr)
        spe = list(spe_arr)
        
        s = []
        for i in range(0, len(pos)):
            # calculate time left to reach destination
            miles_remaining = target - pos[i]
            time_remaining = miles_remaining / spe[i]
            
            # if stack is empty, add time to stack
            if len(s) == 0:
                s.append(time_remaining)
            # if time remaining is less than time at top of stack, add to stack
            elif time_remaining < s[-1]:
                s.append(time_remaining)
            else:
                # while stack is not empty and time remaining is more or equal
                # to top of stack time, pop stack
                while len(s) > 0 and time_remaining >= s[-1]:
                    s.pop()
                # then add the time
                s.append(time_remaining)

        return len(s)
