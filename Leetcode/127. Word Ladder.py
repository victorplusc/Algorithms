"""
127. Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # return self.bfs(beginWord, endWord, wordList)
        return self.bidir_bfs(beginWord, endWord, wordList)
    
    # Time complexity: O(M**2*N)
    # Space complexity: O(M**2*N)
    def bidir_bfs(self, beginWord, endWord, wordList):
        def visit_node(q, visited, others_visited):
            front, transforms = q.popleft()
            
            for i in range(n):
                wildcard = front[:i]+"*"+front[i+1:]
                for word in combinations[wildcard]:
                    if word in others_visited:
                        return transforms + others_visited[word]
                    if word not in visited:
                        visited[word] = transforms+1
                        q.append([word, transforms+1])
        
        n = len(beginWord)
        words = set(wordList)
        if n != len(endWord) or not wordList or endWord not in words:
            return 0
        
        words = set(wordList)
        
        combinations = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                combinations[word[:i]+ "*" + word[i+1:]].append(word)
                
        q_begin = collections.deque([[beginWord, 1]])
        q_end = collections.deque([[endWord, 1]])
        
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        
        while q_begin and q_end:
            transforms = visit_node(q_begin, visited_begin, visited_end)
            if transforms: return transforms
            transforms = visit_node(q_end, visited_end, visited_begin)
            if transforms: return transforms
            
        return 0

    # Time complexity: O(M**2*N)
    # Space complexity: O(M**2*N)
    def bfs(self, beginWord, endWord, wordList):
        n = len(beginWord)
        words = set(wordList)
        if n != len(endWord) or not wordList or endWord not in words:
            return 0
        
        combinations = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                combinations[word[:i]+ "*" + word[i+1:]].append(word)
        
        q = collections.deque([[beginWord, 1]])
        visited = set()
        while q:
            front, transforms = q.popleft()
            visited.add(front)
            for i in range(n):
                wildcard = front[:i]+"*"+front[i+1:]
                for word in combinations[wildcard]:
                    if word == endWord:
                        return transforms+1
                    if word not in visited:
                        q.append([word, transforms+1])
        return 0
