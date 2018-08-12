'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def has_sum(l, k):
    l.sort()
    i = 0
    j = len(l)-1
    found = False
    while i < j and not found:
        sum = l[i] + l[j]
        if sum == k:
            found = True
        elif sum > k:
            j -= 1
        elif sum < k:
            i += 1
    return found

if __name__ == '__main__':
    list = [10, 15, 3, 7]
    k = 17
    assert has_sum(list, k)
