"""
721. Accounts Merge
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
# Time complexity: O(sum(a log a)), where a is the length of accounts[i].
#               => O(N*(k log k)) 
# Space complexity: O(sum(a)) => O(N)
"""
Algorithm:

We implicitly label each account from 0..N-1

We create a graph where for every email, we have the email point to a list of indices where the email was seen

Then for every account, dfs such that:
    We iterate over emails at account[i] and for each email, we go through each index where the email also occurs.
    Then sort and combine. Duplicates are processed with the use of a set
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(list) # email: indices, e.g. {"email@.com" : [0, 2]}
        
        for i, account in enumerate(accounts):
            username = account[0]
            for j in range(1, len(account)):
                email = account[j]
                graph[email].append(i)      

        def dfs(idx, emails):
            if idx in visited:
                return
            visited.add(idx)
            for j in range(1, len(accounts[idx])):
                email = accounts[idx][j]
                emails.add(email)
                for nei in graph[email]:
                    dfs(nei, emails)
        
        res = []
        visited = set()
        for i, account in enumerate(accounts):
            if i not in visited:
                name = account[0]
                emails = set()
                
                dfs(i, emails)
                res.append([name] + sorted(emails))
        
        return res
