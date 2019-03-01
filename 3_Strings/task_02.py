# String Split and Join

def split_and_join(line):
    # write your code there
    line = line.split(" ")
    line = "-".join(line)
    return  line

if __name__ == '__main__':
    # line = input()
    line = "this is a string"
    result = split_and_join(line)
    print(result)