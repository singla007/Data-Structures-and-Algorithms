class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_dict = dict()
        for i in S:
            if i in char_dict.keys():
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        ch_list = list()
        count_list = list()
        count = 0
        result_count = 0
        for ch in S:
            result_count += 1
            if ch not in ch_list:
                count += char_dict[ch]
                ch_list.append(ch)
            count -= 1
            if count == 0:
                ch_list == list()
                count_list.append(result_count)
                result_count = 0
        return count_list
