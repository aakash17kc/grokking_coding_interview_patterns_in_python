def group_anagrams(words):
    word_map = {}
    for word in words:
        ch_count = [0]*26
        for c in word:
            ch_count[ord(c)-ord('a')] +=1
        key = tuple(ch_count)
        if key in word_map.keys():
            word_map[key].append(word)
        else:
            word_map[key] = [word]
    if word_map.values() == []:
        return [[]]
    res = []
    for val in word_map.values():
        res.append(val)
    return res