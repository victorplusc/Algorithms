"""
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        neededCharacters = {}
                
        for i in licensePlate:
            if i >= "a" and i <= "z":
                if i not in neededCharacters:
                    neededCharacters[i] = 1
                else:
                    neededCharacters[i] += 1
        
        smallest = ""
        
        for word in words:
            
            enough = True
            temp = {}
        
            for char in word:
                if char in neededCharacters:
                    if char in temp:
                        temp[char] += 1
                    else:
                        temp[char] = 1
            
            try:
                for count in neededCharacters:
                    if neededCharacters[count] > temp[count]:
                        enough = False
                        
                if enough == True and smallest == "":
                    smallest = word
                if enough == True and len(smallest) > len(word):
                    smallest = word
            except:
                pass
            
        return smallest
