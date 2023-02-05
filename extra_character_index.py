def extra_character_index(str1, str2):
    if len(str1) == len(str2):
        return None
    res = 0
    for ch in str1:
        res = res ^ ord(ch)
    for ch in str2:
        res = res ^ ord(ch)
    if len(str1) > len(str2):
        return str1.index(chr(res))
    else:
        return str2.index(chr(res))
