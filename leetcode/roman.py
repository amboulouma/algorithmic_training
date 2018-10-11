def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_to_number = 0
    count = 0
    for i in range(len(s)-1):
        if roman_dict[s[i]] <= roman_dict[s[i+1]]:
            count -= roman_dict[s[i]]
        else:
            roman_to_number += count
            roman_to_number += roman_dict[s[i]]
            count = 0
    if count < 0:
        if s[len(s) - 2] == s[len(s) - 1]:
            return roman_to_number + abs(count) + roman_dict[s[len(s) - 1]]
        elif s[len(s) - 2] < s[len(s) - 1]:
            return roman_to_number + count + roman_dict[s[len(s) - 1]]
    else:
        return roman_to_number


print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("DCXXI"))
