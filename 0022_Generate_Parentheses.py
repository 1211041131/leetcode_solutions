class Solution(object):

    def solve(self, ind, total, bracket, result, n):

        if total < 0 or total > len(bracket) // 2:
            return

        if ind >= len(bracket):
            if total == 0:
                result.append("".join(bracket))
            return

        bracket[ind] = '('
        self.solve(ind + 1, total + 1, bracket, result, n)

        bracket[ind] = ')'
        self.solve(ind + 1, total - 1, bracket, result, n)

    def generateParenthesis(self, n):

        bracket = [""] * (n * 2)
        result = []

        self.solve(0, 0, bracket, result, n)

        return result