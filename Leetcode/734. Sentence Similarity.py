"""
734. Sentence Similarity
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""
# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def areSentencesSimilar(self, words1: [str], words2: [str], pairs: [[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        elif not words1:
            return True
        
        similar_words = {}
        for p, q in pairs:
            if p not in similar_words:
                similar_words[p] = {q}
            else:
                similar_words[p].add(q)
            if q not in similar_words:
                similar_words[q] = {p}
            else:
                similar_words[q].add(p)
        
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                if words1[i] not in similar_words or words2[i] not in similar_words[words1[i]]:
                    return False    
        return True
