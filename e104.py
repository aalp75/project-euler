def add(a: list, b: list) -> list:
    """
    add a and b where a and b are of the form reverse list,
    e.g. 187 is represented as [7, 8, 1]
    """
    res = []
    carry = 0

    na, nb = len(a), len(b)
    n = max(na, nb)

    for i in range(n):
        x = carry
        carry = 0

        if i < na:
            x += a[i]
        if i < nb:
            x += b[i]

        if x >= 10:
            x -= 10
            carry += 1

        res.append(x)

    if carry > 0:
        res.append(carry)

    return res


def check_digits(a: list):
    if a[0] != 1:
        return False
    for i in range(1, len(a)):
        if a[i] != a[i - 1] + 1:
            return False
    return True


def cond(a: list) -> bool:
    if len(a) < 20:
        return False

    end = sorted(a[:9])
    start = sorted(a[-9:])

    if check_digits(start) and check_digits(end):
        return True

    return False


F1 = [1]
F2 = [1]

for i in range(3, 10_000_000):
    Fn = add(F1, F2)
    F1 = F2
    F2 = Fn

    if cond(Fn):
        print(f"F{i}")
        break

# answer: F329468