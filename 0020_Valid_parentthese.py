class Solution(object):
    def isValid(self, s):
        stack =[]
        for bracket in s:
            if bracket=="(" or bracket=="{" or bracket =="[":
                stack.append(bracket)

            else : 
                if len(stack)==0:
                    return False
                
                e=stack.pop()
                if (bracket == ")" and e == "(") or (bracket == "]" and e == "[") or (bracket == "}" and e == "{"):
                    continue 

                else:
                    return False
        if len(stack)==0:
            return True


        else:
            return False