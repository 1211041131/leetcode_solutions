class Solution(object):
    def maxScore(self, cardPoints, k):
        n=len(cardPoints)
        i=0
        j=n-1
        total=0
        while i<k:
            total+=cardPoints[i]
            i+=1
        i-=1
        ans=total
        while i>=0:
            total= total -cardPoints[i] +  cardPoints[j]
            ans=max(total,ans)
            i-=1
            j-=1
        return ans       