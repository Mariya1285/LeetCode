class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = dict(Counter(nums))
        tup = sorted(new_dict.items() , reverse=True, key=lambda x: x[1])
        temp_list = list()
        for i in range(k):
            temp_list.append(tup[i][0])
        return temp_list