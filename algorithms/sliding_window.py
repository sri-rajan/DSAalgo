# SLIDING WINDOW
# Problem: Maximum Sum Subarray of Size K

# Question:
# Find max sum of any subarray of size k.

# Input:
# arr = [2,1,5,1,3,2]
# k = 3

# Output:
# 9

# Explanation:
# [5,1,3] = 9


def maxSumSUbArray(arr, k):
    windowSum = 0
    maxSum = 0
    for i in range(k):
        windowSum += arr[i]
    maxSum = windowSum
    for right in range(k, len(arr)):
        windowSum += arr[right]
        windowSum -= arr[right - k]
        maxSum = max(maxSum, windowSum)
    return maxSum


answer = maxSumSUbArray([2, 1, 5, 1, 3, 2], 3)
print("this is answer", answer)
