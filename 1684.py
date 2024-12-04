class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # iterate through words
        # iterate through each character in word
        # if character is not in allowed
        # break to next word
        # elif word completes and no break, add to allowed_words
        count = 0
        for word in words:
            allowed_word = True
            for char in word:
                if char not in allowed:
                    allowed_word = False
                    break
            if allowed_word:
                count += 1
        return count
                
