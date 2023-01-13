class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        #refer: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/discuss/1955433/JavaC%2B%2BPython-DFS-on-Tree
        tree = defaultdict(list)
        
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        
        #to store ans globally and not pass it in the function
        res = [-1]
        
        def dfs(node):
            candi = [0]
            
            for nei in tree[node]:
                cur = dfs(nei)
                if s[nei] != s[node]:
                    candi.append(cur)
            
            candi = nlargest(2, candi)
            res[0] = max(res[0], sum(candi) + 1)
            return max(candi) + 1
        
        dfs(0)
        return res[0]