def calculator(expression):
    number = 0
    sign = 1
    res = 0
    stack = []

    for c in expression:
        if c.isdigit():
            number = number * 10 + int(c)
        elif c in "+-":
            res = res + (number * sign)
            sign = -1 if c == '-' else 1
            number = 0
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            prev_sign = stack.pop()
            prev_val = stack.pop()
            res = res + (number * sign)
            res = res * prev_sign
            res = res + prev_val
            number = 0
    return res + (number * sign)

if __name__ == '__main__':
    print(calculator("12 - (6 + 2) + 5"))