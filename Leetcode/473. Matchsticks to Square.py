class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_value = sum(matchsticks)
        if total_value%4 != 0: return False
        side_length = total_value//4
        
        matchsticks.sort(reverse=True)
        def dfs(sides, i=0):
            if i==len(matchsticks):
                if sum(sides) == 0:
                    return True
                else:
                    return False

            curr = matchsticks[i]

            for j, side in enumerate(sides):
                if side-curr >= 0:
                    sides[j] -= curr
                    if dfs(sides, i+1): 
                        return True
                    sides[j] += curr
            return False

        return dfs([side_length]*4)
