def countingValleys(n, s):
    alt = 0
    valleys = 0
    for c in s:
        if c == "U": 
            alt += 1
            if alt == 0: valleys += 1
        else:
            alt -= 1
    return valleys
