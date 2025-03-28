# 1. Find pair that sums up to K

Given an array of integers arr and an integer k, create a boolean function that checks if there exist two elements in arr such that we get k when we add them together.

Example 1:
Input: arr = [4, 5, 1, -3, 6], k = 11
Output: true
Explanation: 5 + 6 is equal to 11

Example 2:
Input: arr = [4, 5, 1, -3, 6], k = -2
Output: true
Explanation: 1 + (-3) is equal to -2

Example 3:
Input: arr = [4, 5, 1, -3, 6], k = 8
Output: false
Explanation: there is no pair that sums up to 8

# 2. First repeating character

Given a string str, create a function that returns the first repeating character.
If such character doesn't exist, return the null character '\0'.

Example 1:
Input: str = "inside code"
Output: 'i'

Example 2:
Input: str = "programming"
Output: 'r'

Example 3:
Input: str = "abcd"
Output: '\0'

Example 4:
Input: str = "abba"
Output: 'b'

# 3. Remove duplicates

Given an array of integers arr, create a function that returns an array containing the values of arr without duplicates (the order doesn't matter).

Example 1:
Input: arr = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
Output: [4, 2, 5, 3, 1]

Example 2:
Input: arr = [1, 1, 1, 1, 1, 1, 1, 1]
Output: [1]

Example 3:
Input: arr = [4, 4, 2, 3, 2, 2, 4, 3]
Output: [4, 2, 3]

# 4. Find the duplicate

Given an array of integers arr that contains n+1 elements between 1 and n inclusive, create a function that returns the duplicate element (the element that appears more than once). Assume that:

- There is only one duplicate number
- The duplicate number can be repeated more than once

Example 1:
Input: arr = [4, 2, 1, 3, 1]
Output: 1

Example 2:
Input: arr = [1, 4, 2, 2, 5, 2]
Output: 2
