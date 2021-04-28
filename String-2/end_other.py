# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring
# upper/lower case differences (in other words, the computation should not be "case sensitive"). Note:
# s.lower() returns the lowercase version of a string.
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    aLen = len(a)
    bLen = len(b)
    a = a.lower()
    b = b.lower()

    if aLen < bLen:
    if b[bLen-aLen:bLen] == a:
        return True
    elif a[aLen-bLen:aLen] == b:
    return True

    return False
