def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rev_s = s[::-1]
    previous_roman = 0
    val = 0
    for i in range(len(s)):
        roman_int = roman_dict[rev_s[i]]
        if roman_int < previous_roman:
            val -= roman_int
        else:
            val += roman_int
        previous_roman = roman_int
    return val


print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("DCXXI"))
print(romanToInt("CXC"))

