class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        f = 0
        l = 0
        lis = list()
        dic = dict()
        longest = list()
        while l != n:
            if s[l] in dic:
                temp = lis.pop(0)
                dic.pop(temp)
                f = f + 1

            else:
                lis.append(s[l])
                dic[s[l]] = 1
                l = l + 1
                if len(lis) > len(longest):
                    longest = lis.copy()
                    print(longest)
        # s_result = ''
        # for i in longest:
        #     s += i
        return len(longest)