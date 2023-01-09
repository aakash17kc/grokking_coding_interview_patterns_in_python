def find_repeated_sequences(s, k):
    # your code will replace this placeholder return statement
    sets = set()
    res = set()
    sets.add(s[0:k])
    for i in range(1, len(s)):
        sub = s[i:i + k]
        if sub in sets:
            res.add(sub)
        sets.add(sub)
    return res

if __name__ == '__main__':
    find_repeated_sequences("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT",10)
