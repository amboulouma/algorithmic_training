def string_splosion(str):
    s=''
    i=1
    for i in range(len(str)+1):
        s+= str[:i]
    return s
print(string_splosion("Code"))