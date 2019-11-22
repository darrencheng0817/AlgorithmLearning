class Solution:
    def myAtoi(self, str: str) -> int:
        res = 0
        flag = 1
        hasNumberFlag = False
        for s in str:
            if s.isdigit():
                res = res * 10 + int(s)
                hasNumberFlag = True
            elif s == "-" and hasNumberFlag == False:
                flag = -1
                hasNumberFlag = True
            elif s == "+" and hasNumberFlag == False:
                flag = 1
                hasNumberFlag = True
            elif s == " " and hasNumberFlag == False:
                pass
            else:
                return self.handleOverflow(res * flag)
        return self.handleOverflow(res * flag)

    def handleOverflow(self, n: str) -> int:
        if n > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if n < -2 ** 31:
            return -2 ** 31
        return n

s = Solution()
assert(s.myAtoi("42") == 42)
assert(s.myAtoi("-42") == -42)
assert(s.myAtoi("-4-2") == -4)
assert(s.myAtoi("w-42") == 0)
assert(s.myAtoi("42e") == 42)
assert(s.myAtoi(" 42e") == 42)
assert(s.myAtoi("+42e") == 42)
assert(s.myAtoi("+ 42e") == 0)