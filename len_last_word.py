def lengthOfLastWord(self, s: str) -> int:
        longest_word = 0
        i = len(s) - 1
        while i>=0 and s[i] == ' ':
            i -=1
        while i>=0 and s[i] != ' ':
            longest_word +=1
            i -=1
        return longest_word 