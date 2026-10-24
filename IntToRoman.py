def toRoman(num: int) -> int:
    my_dict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    results = []

    for roman, value in my_dict.items():
        if num == 0:
            return "".join(results)
        else:
            while (value <= num):
                results.append(roman)
                num = num - value

    return "".join(results)


if __name__ == "__main__":
    print(toRoman(3999))
