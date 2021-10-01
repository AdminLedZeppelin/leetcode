class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not strs:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
'''
复杂度分析

    时间复杂度：O(mn)O(mn)O(mn)，其中 mmm 是字符串数组中的字符串的平均长度，nnn 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。

    空间复杂度：O(1)O(1)O(1)。使用的额外空间复杂度为常数。
 
'''