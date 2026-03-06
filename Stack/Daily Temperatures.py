# Daily Temperatures: https://neetcode.io/problems/daily-temperatures/question?list=neetcode150

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    	days_before_warm = []
    	n = len(temperatures)
    	for i in range(n):
    		current_temp = temperatures[i]
    		cold_days = 0
    		found_warm = False
    		for j in range(i + 1, n):
    			if temperatures[i] >= temperatures[j]:
    				cold_days += 1
    			else:
    				found_warm = True
    				break
    		if found_warm :
    			days_before_warm.append(cold_days + 1)
    		else: 
    			days_before_warm.append(0)
    	return days_before_warm