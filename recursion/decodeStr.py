class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        numstack = []
        strstack = []
        num = ''
        for index in range(len(s)):
            if s[index].isdigit():
                num += s[index]
            elif s[index] == '[':
                numstack.append(int(num))
                strstack.append('[')
                num = ''
            elif s[index] == ']':
                start = -1
                while strstack[start] != '[':
                    start -= 1
                temp = strstack[start + 1:]                
                strstack = strstack[:start]
                for times in range(numstack.pop()):
                    for e in temp:
                        strstack.append(e)
            else:
                strstack.append(s[index])

        res = ''.join(str(x) for x in strstack)
        return res

        
        
        # res = ''
        # num = 0
        # i = 0
        # while i < (len(s)):
        #     if s[i].isdigit():
        #         num = num*10 + int(s[i])
        #     elif s[i] == '[':
        #         start = i + 1
        #         sta = []
        #         while i < len(s):
        #             if s[i] == '[':
        #                 sta.append('[')
        #             if s[i] == ']':
        #                 sta.remove('[')
        #             if not sta:
        #                 break
        #             i += 1
        #         end = i
                
        #         temp = self.decodeString(s[start:end])
        #         for times in range(num):
        #             res += temp

        #         num = 0
        #     else:
        #         res += s[i]
            
        #     i += 1
        
        # return res

s = "10[leetcode]"

sol = Solution()
res = sol.decodeString(s)
print(res)

print(int('0'))