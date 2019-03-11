class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        allEmails = set()
        
        for email in emails:
            separated = email.split("@")
            new = []
            for char in separated[0]:
                if char != ".":
                    new.append(char)
                if char == "+":
                    break
            new.append(separated[1])
            allEmails.add("".join(new))
        
        return len(allEmails)
