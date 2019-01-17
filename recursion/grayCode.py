class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        res = self.grayCode(n-1)

        addon = pow(2, n-1)

        i = pow(2, n-1) - 1
        while i >=0:
            res.append(res[i] + addon)
            i -= 1
            
        return res
    