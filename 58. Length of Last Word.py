#58. Length of Last Word

def lengthOfLastWord(s):
    try:
        return len(s.split()[len(s.split())-1])
    except:
        return 0
