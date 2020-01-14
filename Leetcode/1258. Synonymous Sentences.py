"""
1258. Synonymous Sentences
Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.
 
Example 1:

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
synonyms[0] != synonyms[1]
All words consist of at most 10 English letters only.
text is a single space separated sentence of at most 10 words.
"""
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # return self.bfs(synonyms, text)
        return self.union_find(synonyms, text)
    
    # Time complexity: O(N!)
    # Space complexity: O(N!)
    def bfs(self, synonyms, text):
        graph = collections.defaultdict(dict)
        queue = collections.deque()
        sentences = set()
        queue.append(text)
        
        for p, q in synonyms:
            graph[p][q] = 1
            graph[q][p] = 1
        
        while queue:
            perm = queue.popleft()
            sentences.add(perm)
            words = perm.split()
            for i, word in enumerate(words):
                if word in graph.keys():
                    for w in graph[word]:
                        new_perm = " ".join(words[:i] + [w] + words[i+1:])
                        if new_perm not in sentences:
                            queue.append(new_perm)
        return sorted(list(sentences))
    
    # Time complexity: O(N log N + N!)
    # Space complexity: O(N!)
    def union_find(self, synonyms, text):
        uf = UnionFind()
        for p, q in synonyms:
            uf.union(p, q)
        words = text.split()
        sentences = []
        self.backtrack(0, [], sentences, uf, words)
        return sentences
        
    def backtrack(self, i, sequence, sentences, uf, words):
        if i == len(words):
            sentences.append(" ".join(sequence))
            return
        r = uf.find(words[i])
        for s in sorted([x for x in uf.classes.keys() if uf.find(x) == r]):
            self.backtrack(i+1, sequence + [s], sentences, uf, words)
        
class UnionFind:
    def __init__(self):
        self.classes = {}
    
    def find(self, x):
        if x not in self.classes:
            self.classes[x] = x
        return self.classes[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if px > py:
            px, py = py, px
        for c, r in self.classes.items():
            if r == py:
                self.classes[c] = px
