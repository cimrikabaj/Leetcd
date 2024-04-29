class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         prefix = ""
         strs.sort()
         for i in range(len(strs[0])):
            if i < len(strs[-1]) and i < len(strs[0]) and strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break

         return prefix