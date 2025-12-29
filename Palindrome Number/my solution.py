class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        #y = int(x)
        #x = int(x)

        if y == x:
            return True
        else:
            return False


