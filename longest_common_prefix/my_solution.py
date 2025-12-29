
class Solution:

    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """this function finds and returns the longest common prefix in a list of strings"""
        goodCharacter = True
        count = 0
        #creates a string 'finalString' which will be printed at the end of the function
        finalString = ''
        while goodCharacter == True:
            checkList = []
            #pulls the 'count' character from each string in 'strs' and puts them into a new list 'checkList'
            for string in strs:
                checkList.append(string[count])
            #assigns a variable checkCharacter to the first character in checkList
            checkCharacter = checkList[0]
            
            for character in checkList:
                #if any character in checkList is unequal to checkCharacter, return finalString
                if character != checkCharacter:
                    goodCharacter = False
                    return finalString
            #if all the characters in checkList are the same, append the first character in checkList to finalString
            #and increase count by one, so the next character in strs can be examined
            finalString = finalString + checkList[0]
            count += 1





