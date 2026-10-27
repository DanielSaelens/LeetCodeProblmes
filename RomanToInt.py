def romanToInt(s: str) -> int:
    my_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

    counter = 0
    i = 0

    while i < len(s):
        if s[i:i + 2] in my_dict:
            counter += my_dict[s[i:i + 2]]
            i += 2
        elif s[i] in my_dict:
            counter += my_dict[s[i]]
            i += 1

    return counter


if __name__ == "__main__":
    print(romanToInt("III"))
    print(romanToInt("XIV"))
    print(romanToInt("MCMXCIV"))
