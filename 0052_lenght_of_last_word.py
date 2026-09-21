class Solution(object):
    def lengthOfLastWord(self, s):

        count = 0
        for ch in s[::-1]:
            if ch == " ":
                if count > 0:
                    break
                continue
            count += 1

        return count