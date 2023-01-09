def min_window(str1, str2):
    # write your code here
    mi = 980980889098
    ind1 = ind2 = 0
    while ind1 < len(str1):
        if str1[ind1] == str2[ind2]:
            ind2 = ind2 + 1
            if ind2 == len(str2):
                ind2 = ind2 - 1
                start = ind1
                end = start + 1
                while ind2 >= 0:
                    if str1[start] == str2[ind2]:
                        ind2 = ind2 - 1
                    start = start - 1
                mi = min(mi, end - start)
                ind2 = ind2+1
        ind1 = ind1 + 1
    return mi


if __name__ == '__main__':
    min_window("abcdebdde", "bde")
