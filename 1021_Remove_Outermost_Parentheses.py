class Solution(object):
    def removeOuterParentheses(self, s):
        stack=[]
        ans=""
        for bracket in s:
            if bracket=="(":
                stack.append(bracket)
                if len(stack)>1:
                    ans+=bracket
            
            else:
         
                e=stack.pop()
                if len(stack)>0:
                    ans+=bracket
                
        return ans


        