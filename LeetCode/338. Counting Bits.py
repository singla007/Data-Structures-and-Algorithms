class Solution:
    def countBits(self, num: int) -> List[int]:
        result = list()
        for i in range(0,num+1):
            result.append(sum(list(map(int,bin(i)[2:]))))
        return result

# class Solution(object):
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         res = [0]
#         while len(res) <= num:
#             res += [i+1 for i in res]
#         return res[:num+1]