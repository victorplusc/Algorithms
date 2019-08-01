""
In an American football game, a play can lead to 2 points (safety), 3 points (field goal), or 7 points (touchdown, assuming the extra point). Many different combinations of 2, 3, and 7 point plays can make up a final score.

Write a program that takes a final score and scores for individual plays, and returns the number of combinations of plays that result in the final score.
"""

## Base solution
# Time complexity O(s*n), s -> number of scores, n -> final score
# Space complexity O(s*n)
def num_score_combinations(final_score: int, play_scores: [int]) -> int:
    
    combinations_for_score = [[1] + [0] * final_score for _ in play_scores]
    
    for i in range(len(play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (combinations_for_score[i-1][j])
            if j >= play_scores[i]:
                with_this_play = combinations_for_score[i][j-play_scores[i]]
            else:
                with_this_play = 0
                
            combinations_for_score[i][j] = without_this_play + with_this_play
            
    return combinations_for_score[-1][-1]
