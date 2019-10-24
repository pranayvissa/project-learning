#!/usr/bin/python

def remove_duplicates(array):
    """
    Remove all duplicates except first one
    """
    curr_l = 0
    arr_l = len(array)
    if arr_l == 0:
        return 0
    elif arr_l == 1:
        return 1

    count = 0
    idx = 0
    while(1):
        if (count == (arr_l-1)):
            break

        if array[idx] == array[idx+1]:
            del array[idx+1]
        else:
            curr_l += 1
            idx += 1
        count += 1

    return len(array)


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    n = len(prices)
    if n <= 1:
        return 0

    diff = [0] * n
    for i in range(1,n):
        diff[i] = prices[i] - prices[i-1]

    profit = 0
    for a in diff:
        if a > 0:
            profit += a
    print profit


def array_rotation(array, pos):
    """
    Rotate array 'pos' times
    """
    if array is None:
        return array

    array_len = len(array)
    if array_len == 0:
        return array
    elif len(array) == 1:
        return array

    for cnt in range(pos):
        array = [array[(array_len-1)]] + array[:(array_len-1)]

    print array


def is_duplicate(array):
    """
    Check if duplicates do not exist
    """
    if len(array) == 0 or len(array) == 1:
        return True

    elements = {}
    for val in array:
        if val in elements:
            return False
        else:
            elements[val] = 1

    return True


def find_single(array):
    """
    Find only single element in array. Everyhting else must be twice
    """
    if len(array) == 1:
        return array[0]

    single = array[0]
    for idx in range(1, len(array)):
        single = single ^ array[idx]

    return single


def find_intersection(array1, array2):
    """
    Find intersection between 2 arrays
    """
    array1.sort()
    array2.sort()

    array1_l = len(array1)
    array2_l = len(array2)

    idx1 = 0
    idx2 = 0
    result = []

    while idx1 < array1_l and idx2 < array2_l:
        if array1[idx1] == array2[idx2]:
            result.append(array1[idx1])
            idx1 += 1
            idx2 += 1
        elif array1[idx1] < array2[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    print result


def move_zeros(array):
    """
    Move all zeros to the end
    """
    array_l = len(array)
    if array_l == 1:
        return array

    for idx in range(array_l):
        if array[idx] == 0:
            del array[idx]
            array.append(0)

    print array


def two_sums(array, target):
    """
    Find pairs of numbers which add up to the target
    """
    vals = {}
    result = []
    arr_l = len(array)
    if arr_l < 2:
        return result

    vals[array[0]] = 1

    for idx in range(1, arr_l):
        val = array[idx]
        var_diff = target - val
        if var_diff in vals:
            result.append([val, var_diff])

        vals[val] = 1

    print result




arr1 = [1,2,2,1]
arr2 = [2,2]

two_sums([3, 5, 2, -4, 8, 11], 7)


