class Solution:
    def addBinary(self, a: str, b: str) -> str:

        sum_int = int(a, 2) + int(b, 2)
        
        return bin(sum_int)[2:]


    def addBinary_manual(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = ''

        while i >= 0 or j >= 0 or carry:
            # Get digit values using character comparison
            if i >= 0:
                digit_a = 1 if a[i] == '1' else 0
            else:
                digit_a = 0

            if j >= 0:
                digit_b = 1 if b[j] == '1' else 0
            else:
                digit_b = 0

            #Three cases: 1+1, 0+0, 1+0 (or 0+1)
            if digit_a == 1 and digit_b == 1:
                # 1 + 1 = 10 in binary
                if carry == 1:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = 1
            elif digit_a == 0 and digit_b == 0:
                # 0 + 0 = 0
                if carry == 1:
                    result = '1' + result
                    carry = 0
                else:
                    result = '0' + result
            else:
                # 1 + 0 or 0 + 1
                if carry == 1:
                    result = '0' + result
                    carry = 1
                else:
                    result = '1' + result

            i -= 1
            j -= 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("1010","1011"))
    print(sol.addBinary_manual("1010","1011"))