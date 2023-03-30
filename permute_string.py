def swap(string, i, index):
    chars = list(string)
    chars[i], chars[index] = chars[index], chars[i]
    return ''.join(chars)


def permute_string(str_val):
    n = len(str_val)
    res = []

    def backtraack(index=0, string=str_val):
        if index == len(string) - 1:
            res.append(string)
            return
        for i in range(index, len(string)):
            swapped_string = swap(string, i, index)
            backtraack(index + 1, swapped_string)

    backtraack()
    return res


def swap_char(word, i, j):
    swap_index = list(word)
    swap_index[i], swap_index[j] = swap_index[j], swap_index[i]
    return ''.join(swap_index)


def permute_string_rec(word, current_index, result):
    if current_index == len(word) - 1:
        result.append(word)
        return

    for i in range(current_index, len(word)):
        swapped_str = swap_char(word, current_index, i)
        permute_string_rec(swapped_str, current_index + 1, result)


def permute_word(word):
    result = []
    permute_string_rec(word, 0, result)
    return result


if __name__ == '__main__':
    print(permute_string("abcde"))
