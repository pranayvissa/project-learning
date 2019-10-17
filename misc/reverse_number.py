#!/usr/bin/python

def reverse_number(num):
    rev = 0
    is_neg = False

    if num == 0:
        return
    elif num < 0:
        is_neg = True
        num = num * -1
    while (num > 0):
        rev = (rev*10) + (num%10)
        num = num/10

    if is_neg:
        rev = rev * -1

    return rev

print reverse_number(-102)
