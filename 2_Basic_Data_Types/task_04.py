# Lists

if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        s = input().split()
        if s[0] == 'insert':
            list.insert(int(s[1]), int(s[2]))
        elif s[0] == 'print':
            print(list)
        elif s[0] == 'remove':
            list.remove(int(s[1]))
        elif s[0] == 'append':
            list.append(int(s[1]))
        elif s[0] == 'sort':
            list.sort()
        elif s[0] == 'pop':
            list.pop()
        elif s[0] == 'reverse':
            list.reverse()
        else:
            print("Error")