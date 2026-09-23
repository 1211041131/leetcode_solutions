class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)

        maxi = arr[n-1]

        for i in range(n-2, -1, -1):
            old = arr[i]
            arr[i] = maxi
            maxi = max(maxi, old)

        arr[n-1] = -1

        return arr