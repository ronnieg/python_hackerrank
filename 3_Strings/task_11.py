# Capitalize

# Complete the solve function below.
def solve(s):
    l = []
    n = s.split(" ")
    for i in n:
        l.append(i.capitalize())
    s = " ".join(str(x) for x in l)
    return s