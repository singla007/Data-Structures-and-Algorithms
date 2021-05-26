class Solution:
    def last_one(self, arr):
        first = 0
        last = len(arr)
        while first <= last:
            mid = (first + last) // 2
            if arr[mid] == 1:
                if (mid + 1) < len(arr) and arr[mid + 1] == 1:
                    first = mid + 1
                else:
                    return mid
            elif arr[mid] == 0:
                last = mid - 1
        return -1

    def tuple_second_ele_sort(self, tup):
        return tup[1]

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_tuple = list()
        for ind, i in enumerate(mat):
            print(self.last_one(i))
            soldiers_tuple.append((ind, self.last_one(i) + 1))
        soldiers_tuple.sort(key=self.tuple_second_ele_sort)
        return [i[0] for i in soldiers_tuple[:k]]