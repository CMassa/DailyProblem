'''
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def get_product(list):
    l = len(list)
    first = [1] * l
    second = [1] * l
    for i in range(1, l):
        first[i] = first[i-1]*list[i-1]
        second[l-i-1] = second[l-i]*list[l-i]
    return [a*b for a,b in zip(first, second)]

if __name__ == '__main__':
    # test 1
    list1 = [1, 2, 3, 4, 5]
    answer1 = [120, 60, 40, 30, 24]
    assert get_product(list1) == answer1

    # test 2
    list2 = [3, 2, 1]
    answer2 = [2, 3, 6]
    assert get_product(list2) == answer2
