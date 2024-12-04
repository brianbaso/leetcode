class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # iterate through words
        # for each word, check if char exists
        # if char exists, add i to answer idx list
        arr = []
        for i in range(len(words)):
            if x in words[i]:
                arr.append(i)
        return arr
