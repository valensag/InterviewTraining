# 5. Two Sum

Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.

Input:
A list of integers nums .
A target integer target.

Output:
A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].

Example:

Input: nums = [5, 1, 7, 2, 9, 3], target = 10
Output: [1, 4]
Explanation: The numbers at indices 1 and 4 in the array add up to the target 10.

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: The numbers at indices 1 and 2 in the array add up to the target 6.

Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: The numbers at indices 0 and 1 in the array add up to the target 6.

Input: nums = [2, 1, 2, 7, 11, 15], target = 9
Output: [2, 3]
Explanation: Notice there are two 2s in the array. The second one will be used.

Input: nums = [1, 2, 3, 4, 5], target = 10
Output: []
Explanation: There are no two numbers in the array add up to the target 10.

Input: nums = [], target = 0
Output: []
Explanation: There are no numbers in the input array, so the function returns an empty list [].

# Remove Duplicates

You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.

You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.

Your function should not modify the original list, instead, it should create a new list with unique values and return it.

Example:
Input:
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Note:

The order of the elements in the updated list may be different from the original list, as sets are unordered.

# Has unique chars

Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.

# Find Pairs

You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs. Assume that each array does not contain duplicate values.

The tests for this exercise assume that arr1 is the list being converted to a set.

Input
Your function should take in the following inputs:

arr1: a list of integers
arr2: a list of integers
target: an integer

Output
Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.

# Longest Consecutive Sequence

Given an unsorted array of integers, write a function that finds the length of the longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
