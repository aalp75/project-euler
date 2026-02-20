def check(curr, x):
    if sum([int(c) for c in str(curr)]) == x:
        return True
    return False


ans = []

for x in range(2, 100):
    curr = x
    for p in range(2, 15):
        curr *= x
        if check(curr, x):
            ans.append(curr)

ans.sort()
print(len(ans))
print(f'{ans[29]:,}')