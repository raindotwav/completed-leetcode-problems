class Solution:
    def isPalindrome(self, x: int) -> bool:
        """This function uses some math to identify if an integer x is a palindrome"""
        """This version of my solution exists because leetcode challenges you to also make a solution without converting x to a string"""
        
        #initialize an empty list to store every digit of x
        mylist = []
        #a copy of x is made to do math without changing the value of x
        y = x
        #negative numbers can never be palindromes, so if x is less than 0, return false
        if x < 0:
            return False
        
        
        
        while y != 0:
            #a variable 'preserve' is created to help do some math while assigning the 'z' variable
            preserve = y
            #this loop divides y by 10, then uses int() to floor it.
            #after it's been floored, we remultiply it by 10 to get the same number without the lastmost digit
            #ex. 123 -> 120
            y = int(y / 10) * 10
            #the z variable takes the value from the beginning on the loop, and subtracts the new value of y
            #ex. 123 - 120
            z = preserve - y
            #we undo the *10 so we can find the next digit on the next loop
            y = int(y /10)
            #this new value in z is then appended to the list created earlier
            mylist.append(z)
        
        
        
        #once we finally have our completed list, we check if it's the same when flipped around
        if mylist == mylist[::-1]:
            return True
        else:
            return False
        


        

