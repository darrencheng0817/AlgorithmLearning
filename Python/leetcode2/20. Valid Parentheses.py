class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if not stack or stack[-1] != char:
                    return False
                stack.pop()
        if stack:
            return False
        return True

s = Solution()
print(s.isValid("()"))