#!/usr/bin/python

def firstUniqChar(myString):
    """
    :type s: str
    :rtype: int
    """

    if len(myString) == 0:
        return -1

    occ = {}
    idx = 0
    for ch in myString:
        if ch in occ:
            occ[ch].append(idx)
        else:
            occ[ch] = []
            occ[ch].append(idx)
        idx = idx+1

    ret = -1
    for ch in myString:
        if len(occ[ch]) == 1:
            ret = occ[ch][0]
            break

    return ret


def checkAnagram(str1, str2):
    '''
    Check is str1 is an anagram of str2
    '''

    if len(str1) != len(str2):
        return False

    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    is_anagram = True

    for indx in range(len(str1)):
        if sorted_str1[indx] != sorted_str2[indx]:
            is_anagram = False
            break

    return is_anagram

def checkPalindrome(myString):

    myStr = myString.replace(" ","")
    import re; regex = re.compile('[^a-zA-Z]')
    myStr = regex.sub('', myStr)
    myStr = myStr.lower()
    length = len(myStr)
    is_palindrome = True
    for idx in range(length/2):
        if myStr[idx] != myStr[length-idx-1]:
            is_palindrome = False
            break

    return is_palindrome


print checkPalindrome("race a car")
