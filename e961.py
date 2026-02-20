# Look at the possible mask for number
# because the value of the digit has no impact
# the only thing that care is if it's either a 0 or either a 1

BITS = 18

def clean(number):
    index = 0
    n = len(number)
    for i in range(len(number)):
        if number[i] == "0":
            index = i + 1
        else:
            break

    if index == n:
        return "0"
    return number[index:n]


winning = set()

for mask in range(1, 1 << BITS):
    s = ""

    for b in range(BITS):
        p2 = 1 << b
        if (p2 & mask) == p2:
            s += "1"
        else:
            s += "0"

    s = s[::-1]
    # is s winning?

    s = clean(s)
    n = len(s)

    for i in range(n):  # remove character i
        new = s[0:i] + s[i + 1:n]
        new = clean(new)
        if new not in winning:
            winning.add(s)

ans = 0

for mask in winning:
    count = 1
    for char in mask:
        if char == '1':
            count *= 9
    ans += count

print(f"ans:{ans:,}")