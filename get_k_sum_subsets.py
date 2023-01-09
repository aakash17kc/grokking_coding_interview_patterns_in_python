def get_bit(num, bit):
    temp = 1 << bit
    temp = temp & num
    if temp == 0:
        return 0
    return 1


def get_all_subsets(set_of_integers):
    res = []
    n = len(set_of_integers)
    total_subsets = 2 ** n
    for i in range(total_subsets):
        st = set()
        for j in range(n):
            if get_bit(i, j) == 1 and set_of_integers[j] not in st:
                st.add(set_of_integers[j])
        res.append(list(st))
    return res


def get_k_sum_subsets(set_of_integers, target_sum):
    # Write your code here
    res = []

    subsets = get_all_subsets(set_of_integers)

    for sub in subsets:
        sum = 0
        for k in sub:
            sum += k
        if sum == target_sum:
            res.append(sub)
    return res

if __name__ == '__main__':
    print(get_k_sum_subsets([8, 13, 3, 22, 17, 39, 87, 45, 36] , 47))
