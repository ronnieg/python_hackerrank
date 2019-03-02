# Symmetric Difference
def diff(m, n):
    l = []
    m = set(m)
    n = set(n)
    m1 = list(m.difference(n))
    n1 = list(n.difference(m))
    for i in m1:
        l.append(i)
    for j in n1:
        l.append(j)
    l.sort()
    return l


if __name__ == '__main__':
    m = int(input())
    m_arr = list(map(int, input().split()))
    n = int(input())
    n_arr = list(map(int, input().split()))
    result = diff(m_arr, n_arr)
    for i in result:
        print(i)