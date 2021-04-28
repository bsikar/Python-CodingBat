# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    z = 0
    for i in range(0, len(str)):
    if str[i:i+3] == "cat":
        z += 1
    if str[i:i+3] == "dog":
        z -= 1

    return z == 0
