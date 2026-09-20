class Solution(object):
    def reverseDegree(self, s):
        hash_map={}
        letters = "abcdefghijklmnopqrstuvwxyz"
        result=0
        for i in range(26):
            hash_map[letters[i]] = 26 - i
        i=0
        for i in range(1,len(s)+1):
            pro=hash_map[s[i-1]]*i
            result+=pro
        return result


        

        