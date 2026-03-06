# Top K Frequent Elements: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150

class Solution:

	def sortByValue(self, d: dict[int, int]) -> list[int]:
		l = list()
		l.extend(d.keys())
		length = len(l)
		for _ in range(0, length -1):
			for j in range(0, length -1):
				if d[l[j]] < d[l[j + 1]]:
					l[j], l[j + 1] = l[j + 1], l[j]

		return l


	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		nums_map = dict()

		for n in nums:
			n_val = nums_map.get(n)
			if n_val == None:
				nums_map.update({n: 1})
			else:
				nums_map[n] = n_val+1

		topK = []
		sorted_lst = self.sortByValue(nums_map)
		for i in range(0, k):
			topK.append(sorted_lst[i])

				

		return topK