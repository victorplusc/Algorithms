"""
You are given a (potentially large) List of words. Some of these are compounds, where all parts are also in the List. Example List:

[rockstar, rock, star, rocks, tar, star, rockstars, super, highway, high, way, superhighway]
The task is to identify all combinations where one word is a composite of two or more words from the same list and print or return them.

Example:

rockstar -> rock + star
superhighway -> super + highway
superhighway -> super + high + way

If returning, the output would be a list of lists, e.g.

[[rock, star], [super, highway], [super, high, way],...]
"""

"""
Notes:

e.g. [rockstar, rock, star, rocks, tar]
output: [[rocks, tar], [rock, star]]

Input: a list of words, some words are made up of multiple words
Output: list of combinations of composite words
        rockstar -> [rock, star], [rocks, tar]
        
Can the list have no composites/be empty?
-> return []

Idea:
[rockstar, rock, star, rocks, tar, star, rockstars, super, highway, high, way, superhighway]
map length of the word to a set of words: e.g. 

rockstar:
> word of length 8
> assume we have mapping = { 4: [rock, star, high], ... }
> look up in the mapping from range (length(word)-1) -> 1 are in it?

output = []
q = collections.deque([all_words])
# every element in the queue should look like, [word, []]

while q:
    word, curr_list = q.popleft()
    for i in range(1, len(word)-1):
        if i == len(word)-1:
            if word in mapping[len(word)] and curr_list:
                curr_list.append(word)
                output.append(curr_list)
        if word[:i] in mapping:
            curr_list.append(word[:i])
            q.append(word[i:])

return output

rockstar
   ^
word[:4]
word[4:]
"""
"""
[rockstar, rock, star, rocks, tar]
mapping = {
  3: [tar]
  4: [rock, star]
  5: [rocks]
  8: [rockstar]
}
q = [[rock, []], star, rocks, tar, [star, [rock]]]

while q:
    word, curr_list = rockstar, []
    for i in range(1, 7):
        i = 4
        curr_list.append(rock)
        q.append([star, [rock]])
"""
import collections
def word_decomp(all_words):
    mapping = collections.defaultdict(list)
    
    for word in all_words:
        # if len(word) not in mapping:
        #     mapping[len(word)] = [word]
        mapping[len(word)].append(word)
    
    output = []
    q = collections.deque([[word, []] for word in all_words])
    # every element in the queue should look like, [word, []]
    
    while q:
        word, curr_list = q.popleft()
        for i in range(1, len(word)):
            if i == len(word)-1:
                if word in mapping[len(word)] and curr_list:
                    output.append(curr_list + [word])
            elif i in mapping and word[:i] in mapping[i]: # O(K), where K is the length of the word
                q.append([word[i:], curr_list + [word[:i]]])

    return output

print(word_decomp(["rockstar", "rock", "star", "rocks", "tar", "star", "rockstars", "super", "highway", "high", "way", "superhighway"])) # [[rock, star], [super, highway], [super, high, way],...]
print(word_decomp(["rockstar", "rock", "star", "rocks", "tar"])) # [rock, star], [rocks, tar]
print(word_decomp(["rock", "star", "rocks", "tar"])) # []
print(word_decomp([]))
