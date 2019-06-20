# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        for i in range(len(s)):
            char = s[i]
            if char in seen:
                seen[char] = (seen[char][0]+1, seen[char][1])
            else:
                #(count,index)
                seen[char] = (1,i)
        seen_order = list(seen)
        for char in seen_order:
            if seen[char][0] == 1:
                return seen[char][1]
        return -1