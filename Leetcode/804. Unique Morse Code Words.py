class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [chr(ord('a') + i) for i in range(26)]
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        engToMorse = {alphabet[i]:morse[i] for i in range(26)}
        
        wordSet = set()
        
        for word in words:
            morseWord = []
            for char in word:
                morseWord.append(engToMorse[char])
            wordSet.add("".join(morseWord))
        
        return len(wordSet)
