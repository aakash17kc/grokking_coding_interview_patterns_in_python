# sum of squared of digits = 1

def is_happy_number(n):
    def squared_sum(num):
        sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            sum += digit
        return sum

    slow = n
    fast = squared_sum(n)

    while fast != 1 and fast != slow:
        slow = squared_sum(n)
        fast = squared_sum(squared_sum(n))
    if fast == 1:
        return True
    return False
