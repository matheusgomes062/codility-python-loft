
# Python3 program to count appearances
# of a digit 'd' in range from [0..n]

# write a function:
#  def solution(N)
#  that, given an integer N, return the number of times the digit 1 occurs in decimal representations of all positive integers not exceeding N.

#  For example, given N = 14 the function should return 6, because:
# All the positive integers that do not exceed 13 are 1, 2, ,3 , 4, 5, 6, 7, 8, 9, 10, 11, 12 and 13;

#   digit 1 occurs six times altogether: once in number 1, once in number 10, twice in number 11, once in number 12 and once in number 13.

# Assume that: N is an integer within the range [0... 100,000].

import math


def solution(N):
    count = 0
    for x in range(N + 1):
        while x >= 1:
            if math.floor(x % 10) == 1:
                count += 1
            x /= 10
    return count
