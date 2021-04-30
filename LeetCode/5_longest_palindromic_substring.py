class Solution:
    def longestPalindrome(self, s: str) -> str:
        lgst = ''
        if len(s) == 1:
            return s
        for i in range(0, len(s)):
            temp = s[i]
            for j in range(1, min(i + 1, len(s) - i)):
                if i >= 1 and s[i - j] == s[i + j]:
                    temp = s[i - j] + temp + s[i - j]
                else:
                    break
            temp2 = ''
            for j in range(0, min(i + 1, len(s) - i - 1)):
                if s[i - j] == s[i + j + 1]:
                    temp2 = s[i - j] + temp2 + s[i + j + 1]
                else:
                    break

            if len(temp) > len(lgst):
                lgst = temp
            if len(temp2) > len(lgst):
                lgst = temp2
        return lgst