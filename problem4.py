'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

def find_missing(l):
    l.sort()
    current = 1
    for n in l:
        if n > current:
            return current
        elif n == current:
            current += 1
    return current

if __name__ == '__main__':
    assert find_missing([3, 4, -1, 1]) == 2
    assert find_missing([1, 2, 0]) == 3