
def ransomNote(ransomNote: str, magazine: str) -> bool:
    my_dict = {}
    my_dict2 = {}

    for i in ransomNote:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for j in magazine:
        if j in my_dict2:
            my_dict2[j] += 1
        else:
            my_dict2[j] = 1

    for k, value in my_dict.items():
        if my_dict2.get(k, 0) < value:
            return False

    return True


if __name__ == "__main__":
    a = "ab"
    b = "aab"
    print(ransomNote(a, b))
