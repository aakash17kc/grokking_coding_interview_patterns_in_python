import math


def find_longest_substring(input_string):
    # your code will replace this placeholder return statement
    max_len = -math.inf
    map = {}
    pos= 0
    for i in range(len(input_string)):
        ch = input_string[i]
        if ch in map:
            pos = max(pos,map[ch])
        max_len = max(max_len, i-pos+1 )
        map[ch] = i + 1
    if max_len == -math.inf:
        return -1
    return max_len


if __name__ == '__main__':
    print(find_longest_substring("abcdbea"))
