def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    bases = [2, 3]
    for a in bases:
        if a >= n:
            continue

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


N = 10  # number of digits
ans = 0

# case 0
for i in range(1, 10):
    for p in range(N - 1):
        for j in range(10):
            v = i * 10 ** (N - 1) + j * 10 ** p
            if is_prime(v) and len(str(v)) == N:
                ans += v

# case 1 to 9
# try first to change 1 digit
# if no primes found then try to change 2 digit

for b in range(1, 10):
    base = 0
    for i in range(N):
        base += b * 10 ** i

    # print("base:", base)
    good = False

    # change 1 digit
    for i in range(N):
        for k in range(10):
            v = base - b * 10 ** i + k * 10 ** i
            if is_prime(v) and len(str(v)) == N:
                ans += v
                good = True

    if not good:
        # if not good switch to 2 indices
        for i in range(N):
            for k1 in range(10):
                for j in range(i + 1, N):
                    for k2 in range(10):
                        v = (
                            base
                            - b * 10 ** i
                            + k1 * 10 ** i
                            - b * 10 ** j
                            + k2 * 10 ** j
                        )
                        if is_prime(v) and len(str(v)) == N:
                            ans += v

print(f"Solution is {ans}")