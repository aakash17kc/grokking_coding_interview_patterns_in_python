def backtrack(index, path, digits, digits_mapping, combinations):
    if len(path) == len(digits):

        combinations.append("".join(path))
        return
    letters = digits_mapping[digits[index]]
    if letters:
        for ch in letters:
            path.append(ch)
            backtrack(index + 1, path, digits, digits_mapping, combinations)
            path.pop()


def letter_combinations(digits):
    combinations = []

    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0:
        return []

    #  Mapping the digits to their corresponding letters
    digits_mapping = {
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}

    # Initiate backtracking with an empty path and starting index of 0

    backtrack(0, [], digits, digits_mapping, combinations)
    return combinations


if __name__ == '__main__':
    print(letter_combinations("23"))
