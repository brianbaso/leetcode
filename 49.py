class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # base case:
        if len(strs) == 1:
            return [[strs[0]]]

        # iterate through char in a word
        # build a unique key for the word
        # add the index of the word as the value for the unique key
        d = {}
        for i, word in enumerate(strs):
            key = ''.join(sorted(word))
            # for char in word:
            #     if key == "" or key[-1] <= char:
            #         key += char
            #     else:
            #         key = char + key
            

            if key not in d:
                d[key] = [i]
            else:
                d[key].append(i)
        
        # iterate through each key's array
        # create empty array
        # append strs[i] to the array
        # append array to result
        ans = []
        for arr in d.values():
            group = []
            for idx in arr:
                group.append(strs[idx])
            ans.append(group)
        
        return ans


                    


