class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create defaultdict put into temp
        temp = defaultdict(list)

        # go through all string in strs
        for s in strs:
            # sorted(s) function take string, alphabet sort abc-xyz
            # ''.join put all singular letter of sorted orignal string into 1
            # and put into sortedS
            sortedS = ''.join(sorted(s))
            
            # append said sorted string by its sortedS value
            temp[sortedS].append(s)
            # end of loop and loop back
        
        # temp would looks like this now
        # aaabnn → [banana]
        # aet → [eat, tea, ate]
        # ant → [tan, nat]
        # now return only value, [banana], [eat, tea, ate], ...
        return list(temp.values())