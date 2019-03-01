# Designer Door Mat
#
# N = 9
#
# M = 27

N, M = map(int,input().strip().split())

# print("Size: " + str(N) + " x " + str(M))

n = 0
for i in range(int(N / 2), 0, -1):
    n += 1
    print("-" * (3) * i + ".|." * (n * 2 - 1) + "-" * (3) * i)

print("-" * int((M - 7) / 2) + "WELCOME" + "-" * int((M - 7) / 2))

m = int(N / 2)
for i in range(0, int(N / 2), 1):
    m -= 1
    print("-" * 3  * int(i + 1) + ".|." * (m * 2 + 1) + "-" * 3  * int(i + 1))
