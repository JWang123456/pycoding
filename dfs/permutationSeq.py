import math
class Solution:
    
    count = 0
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        num = []
        visited = set()

        fct = math.factorial(n-1)
        start = k//fct + 1

        self.count += fct * (start - 1)
        num.append(start)
        visited.add(start)

        self.helper(n, k, res, num, visited)
        return res[-1]

    def helper(self, n, k, res, num, visited):

        if len(num) == n:
            self.count += 1
            n = ''.join(str(x) for x in num)
            res.append(n)
            return
        
        for i in range(1, n+1):
            if i in visited:
                continue
            
            num.append(i)
            visited.add(i)
            self.helper(n, k, res, num, visited)
            if self.count == k:
                break
            num.remove(i)
            visited.remove(i)

if __name__ == "__main__":
    
    sol = Solution()

    res = sol.getPermutation(4, 9)

    print(res)

        