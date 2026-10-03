class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort -> index are numbers , their count are values
        count = {} # value : count 
        freq = [[] for i in range(len(nums) + 1)] # count : values , len == max no of elements , max count
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for n,c in count.items():
            freq[c].append(n) # -> count to append them 
        res = []
        for i in range(len(freq)-1,0,-1): # count 
            for n in freq[i] : # if any value at particular index 
                res.append(n)
                if len(res) == k:
                    return res

        
        