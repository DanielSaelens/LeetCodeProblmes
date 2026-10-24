from collections import Counter


def validAnagram(s: str, t: str) -> bool:
    my_dict = {}
    my_dict2 = {}

    for i in s:
        if i in my_dict:
            my_dict[i] += 1

        else:
            my_dict[i] = 1

    for j in t:
        if j in my_dict2:
            my_dict2[j] += 1
        else:
            my_dict2[j] = 1

    if my_dict == my_dict2:
        return True

    return False


def validA(s: str, t: str) -> bool:
    counterS = Counter(s)
    counterT = Counter(t)

    return counterS == counterT


if __name__ == "__main__":
    a = "silent"
    b = "listen"
    print(validAnagram(a, b))
    print(validA(a, b))
