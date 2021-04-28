import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if len(nums1)%2 == 0:
            print((len(nums1)/2)-1)
            return (nums1[int((len(nums1)/2)-1)] + nums1[int(len(nums1)/2)])/2
        else:
            return nums1[math.floor(len(nums1)/2)]