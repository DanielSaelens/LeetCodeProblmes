
def palindrome(s) -> bool:
    target = len(s) - 1
    i = 0
    is_palindrome = True

    while i < target:
        if s[i] != s[target]:
            is_palindrome = False
            break
        i += 1
        target -= 1

    if is_palindrome:
        return True
    else:
        return False


print(palindrome("racecar"))