'''Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

https://www.youtube.com/watch?v=wiGpQwVHdE0 '''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left = left + 1
            charSet.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
        