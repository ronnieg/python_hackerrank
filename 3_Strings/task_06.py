# String Validators

def validator(string):
    l = list(string)

    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False

    for i in range(len(l)):
        if l[i].isalnum() == True:
            is_alnum = True

    for i in range(len(l)):
        if l[i].isalpha() == True:
            is_alpha = True

    for i in range(len(l)):
        if l[i].isdigit() == True:
            is_digit = True

    for i in range(len(l)):
        if l[i].islower() == True:
            is_lower = True

    for i in range(len(l)):
        if l[i].isupper() == True:
            is_upper = True

    print(is_alnum)
    print(is_alpha)
    print(is_digit)
    print(is_lower)
    print(is_upper)

if __name__ == '__main__':
    s = input()
    validator(s)