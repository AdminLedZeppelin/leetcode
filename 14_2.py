class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = str[0][i]
            if any(i == len(str[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]





'''
复杂度分析

    时间复杂度：O(mn)O(mn)O(mn)，其中 mmm 是字符串数组中的字符串的平均长度，nnn 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。

    空间复杂度：O(1)O(1)O(1)。使用的额外空间复杂度为常数。
'''