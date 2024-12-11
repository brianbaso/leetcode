class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for word in strs:
            if 0 <= len(word) < 10:
                coded += "1"
            elif 10 <= len(word) < 100:
                coded += "2"
            elif len(word) >= 100:
                coded += "3"
            coded += str(len(word))
            coded += word
        return coded

    # 14neet14code14love13you
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            if s[i] == "1":
                word = ""
                for j in range(i+2, i + 2 + int(s[i+1])):
                    word += s[j]
                decoded.append(word)
                i += len(word)+2

            elif s[i] == "2":
                word = ""
                for j in range(i+3, i + 3 + int(s[i+1:i+3])):
                    word += s[j]
                decoded.append(word)
                i += len(word)+3

            elif s[i] == "3":
                word = ""
                for j in range(i+4, i + 4 + int(s[i+1:i+4])):
                    word += s[j]
                decoded.append(word)
                i += len(word)+4

        return decoded

