# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            opening_brackets_stack.append(Bracket(next, i))
            pass

    length = len(opening_brackets_stack) - 1
    for i in range(0, length):
        if i > opening_brackets_stack[length - i][1]:
            break

        if are_matching(opening_brackets_stack[i][0], opening_brackets_stack[length - i][0]) is not True:
            if are_matching(opening_brackets_stack[i][0], opening_brackets_stack[i + 1][0]) is True:
                continue
            return opening_brackets_stack[i][1] if opening_brackets_stack[i][0] not in ")]}" else opening_brackets_stack[i+1][1]
    
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
