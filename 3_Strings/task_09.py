# String Formatting

def print_formatted(number):
    # for i in range(1, int(number) + 1, 1):
    #     octal = oct(i)[2:]
    #     hexadecimal = hex(i)[2:]
    #     binary = bin(i)[2:].upper()
    #     lens = len(str(binary))
    #     string = "{0} {1} {2} {3}".format(i, octal, hexadecimal, binary)
    #     print('{0:{w}}'.format(string, w = int(lens)))
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        # print("{0:{w}d} {0:{w}o} {0:{w}x} {0:{w}b}".format(i, w=width))
        print(str.rjust(str(i), width), str.rjust('{:o}'.format(i), width), str.rjust('{:X}'.format(i), width), str.rjust(
            '{:b}'.format(i), width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)