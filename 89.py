letter_to_num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

num_to_letter = {v: k for k, v in letter_to_num.iteritems()}


def value_roman(roman):
    if roman == '':
        return 0
    if roman[:2] in letter_to_num:
        return letter_to_num[roman[:2]] + value_roman(roman[2:])
    if roman[:1] in letter_to_num:
        return letter_to_num[roman[:1]] + value_roman(roman[1:])
    raise


def write_roman(num):
    if num in num_to_letter:
        return num_to_letter[num]
    nums = num_to_letter.keys()
    best_num = max(filter(lambda x: x < num, nums))
    return num_to_letter[best_num] + write_roman(num - best_num)

