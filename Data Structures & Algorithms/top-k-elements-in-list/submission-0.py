class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        top_k = []

        for num in nums:
            if num not in dic:
                dic[num] = 1
            dic[num] += 1
        
        sorted_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        
        for tup in sorted_dic:
            top_k.append(tup[0])
        return top_k[:k]
