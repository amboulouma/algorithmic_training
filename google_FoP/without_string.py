def without_string(str, s):
    result = str
    for i in range(str.count(s)):
        result = str.replace(s,'')
    return result

print(without_string("Hello there", "llo"))