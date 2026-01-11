class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        para = { ')':'(', '}':'{', ']':'[' }

        if len(s)%2 != 0:
            return False

        for i in range(len(s)):
            char = s[i]
            if(char in ["[","{","("]):
                stack.append(char)
            
            else:
                if not stack:
                    return False
            
                if(para.get(char) == stack[-1]):  
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
                

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]"))