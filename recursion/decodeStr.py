class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        num = 0
        i = 0
        while i < (len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == '[':
                start = i + 1
                sta = []
                while i < len(s):
                    if s[i] == '[':
                        sta.append('[')
                    if s[i] == ']':
                        sta.remove('[')
                    if not sta:
                        break
                    i += 1
                end = i
                
                temp = self.decodeString(s[start:end])
                for times in range(num):
                    res += temp

                num = 0
            else:
                res += s[i]
            
            i += 1
        
        return res

s = "10[leetcode]"

sol = Solution()
res = sol.decodeString(s)
print(res)

print(int('0'))