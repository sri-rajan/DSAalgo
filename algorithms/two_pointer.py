# TWO POINTER

# Problem: Two Sum in Sorted Array

# Question:
# Given a sorted array, find two numbers that add up to a target.

# Input:
# arr = [2, 7, 11, 15]
# target = 9

# Output:
# [2, 7]


def twoSumSorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        elif sum < target:
            left = left + 1
        else:
            right = right - 1
    return []


answer = twoSumSorted([2, 7, 11, 15], 9)
print("answer", answer)
