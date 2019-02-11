# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    l = list(arr)
    l = set(l)
    l = list(l)
    l.sort()
    print(l[-2])