"""
Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.
"""
#Example:
    #Input: "Let's take LeetCode contest"
    #Output: "s'teL ekat edoCteeL tsetnoc"

def reverseWords(s: "String to be reversed"):
    temp = s.split()
    for i in range(len(temp)):
        if i == len(temp)-1:
            temp[i] = reverseWord(temp[i])
        else:
            temp[i] = reverseWord(temp[i]) + " "
    return "".join(temp)

def reverseWord(word: "String"):
    temp = []
    for i in range(len(word)):
        temp.append(word[len(word)-i-1])
    return "".join(temp)

#Time complexity: O(N)
#Space complexity: O(N)
