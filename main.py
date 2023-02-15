# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    bracket = ""
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass

        if next in ")]}":
            bracket = Bracket(next, i)
            if len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[0][0], bracket[0]) is False:
                return bracket[1] + 1
            else:
                opening_brackets_stack.pop()

    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0][1]
    else:
        return "Success"

def main():
    text = input()
    if (text[0].upper() == "I"):
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
    main()
