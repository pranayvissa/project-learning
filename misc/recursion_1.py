#!/proj/olympus/work/sw/hware/tools/centos-7/bin/python

# Reverse a String
def ReverseString(string):
    if len(string) == 0:
        return string
    else:
        return ReverseString(string[1:]) + string[0]


def ReverseList(thislist):
    if len(thislist) == 0:
        return thislist
    else:
        return ReverseList(thislist[1:]) + [thislist[0]]

print ReverseString("Hello")

thislist = ['h','e','l','l','o']
print ReverseList(thislist)

