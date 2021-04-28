# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded
# by a period (.). So "xxyz" counts but "x.xyz" does not.
#
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    z = True
    for i in range(0, len(str)):
    if str[i] == '.':
        z = False
    elif str[i:i+3] == "xyz" and z:
        return True
    else:
        z = True

    return False
