"""
https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python?fbclid=IwAR26NYe2RLcvokZiApCXJLuXoAR3JNJzSZPXVWw7xyYa2kf0NAHkUXWQ3H0
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""


def count_positives_sum_negatives(arr):
    plus_numbers = [number for number in arr if number > 0]
    sum_minus = sum(number for number in arr if number < 0)

    return [] if len(arr) == 0 else [len(plus_numbers), sum_minus]
