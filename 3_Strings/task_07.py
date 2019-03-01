# Text Wrap

import textwrap

def wrap(string, max_width):
    newstring = textwrap.wrap(string, width=max_width)
    return ("\n").join(newstring)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)