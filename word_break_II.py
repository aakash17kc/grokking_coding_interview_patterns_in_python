# catsandog -> cats and dog


def helper(s, word_dict, result):
    if not s:
        return []
    if s in result:
        return result[s]
    res = []
    for word in word_dict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(s)
        else:
            rest_of_words = helper(s[len(word):], word_dict, result)
            for item in rest_of_words:
                temp = word + ' ' + item
                res.append(temp)
    result[s] = res
    return res


def word_break(s, word_dict):
    return helper(s, word_dict, {})
