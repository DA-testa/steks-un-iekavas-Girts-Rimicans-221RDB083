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

    bad_pos = []
    length = len(opening_brackets_stack) - 1
    for i in range(0, length):
        if len(bad_pos):
            if are_matching(opening_brackets_stack[bad_pos[0]][0], opening_brackets_stack[bad_pos[1]][0]) is True:
                return opening_brackets_stack[bad_pos[1]][1] if opening_brackets_stack[bad_pos[1]][0] not in ")]}" else opening_brackets_stack[bad_pos[1]+1][1]
            return opening_brackets_stack[bad_pos[1]][1] if opening_brackets_stack[bad_pos[1]][0] in ")]}" else opening_brackets_stack[bad_pos[1]+1][1]
        else:
            if i > opening_brackets_stack[length - i][1]:
                break

            if are_matching(opening_brackets_stack[i][0], opening_brackets_stack[length - i][0]) is not True:
                if are_matching(opening_brackets_stack[i][0], opening_brackets_stack[i + 1][0]) is True:
                    continue
                bad_pos = [i, length - 1]
                if i == (length - 1):
                    return opening_brackets_stack[i][1] if opening_brackets_stack[i][0] not in ")]}" else opening_brackets_stack[i+1][1]

    return "Success"


def main():
    # text = input()
    text = "[({])}"
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
