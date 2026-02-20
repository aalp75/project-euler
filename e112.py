def is_increasing(x):
    x = str(x)
    n = len(x)
    for i in range(1, n):
        if int(x[i]) > int(x[i - 1]):
            return False
    return True


def is_decreasing(x):
    x = str(x)
    n = len(x)
    for i in range(1, n):
        if int(x[i]) < int(x[i - 1]):
            return False
    return True


def is_bouncing(x):
    if is_increasing(x) or is_decreasing(x):
        return False
    return True


E = 0
N = 10_000_000
tot = 0

for i in range(1, N):
    tot += 1
    if is_bouncing(i):
        E += 1

    if E / tot > 0.99:
        print("Solution is", i - 1)
        break