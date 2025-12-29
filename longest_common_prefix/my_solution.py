class Solution:


    def longestCommonPrefix(self, strs: List[str]) -> str:
        #what this function does:
        #creates a string 'finalString' which will be printed at the end of the function
        #pulls the 'count' character from each string in 'strs' and puts them into a new list 'checkList'
        #assigns a variable checkCharacter to the first character in checkList
        #if any character in checkList is unequal to checkCharacter, return finalString
        #if all the characters in checkList are the same, append the first character in checkList to finalString
        #and increase count by one, so the next character in strs can be examined
        goodCharacter = True
        count = 0
        finalString = ''
        while goodCharacter == True:
            checkList = []
            for i in range(len(strs)):
                checkList.append(strs[i][count])
            checkCharacter = checkList[0]
            
            for i in range(len(checkList)):
                if checkList[i] != checkCharacter:
                    goodCharacter = False
                    return finalString
            finalString = finalString + checkList[0]
            count += 1





