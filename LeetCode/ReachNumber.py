class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        n = 1
        ind = target%2
        while True:
            maxSum = n*(n+1)/2
            
            if maxSum >= abs(target) and maxSum%2==ind:
                return n
            n+=1
a = Solution
print(a.reachNumber(a,target = 2))
