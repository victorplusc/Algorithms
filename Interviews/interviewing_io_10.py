def character_replacement(s, k):
    highest_count = 0
    longest = 0
    left = 0
    count = collections.Counter()
    for right, val in enumerate(s):
        count[val] += 1
        highest_count = max(highest_count, count[val])
        to_remove = right-left+1-highest_count
        if to_remove > k:
            count[s[left]] -= 1
            left += 1
        else:
            longest = max(longest, right-left+1)
    return longest
