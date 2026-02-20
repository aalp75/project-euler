import itertools

N = 100
primes = []
is_prime = [True] * N

for i in range(2, N):
    if not is_prime[i]:
        continue
    primes.append(i)
    for j in range(2 * i, N, i):
        is_prime[j] = False

primes = [2, 3, 5, 7]

# Generate all permutations of the numbers 1 through 7
arr = [1, 2, 3, 4, 5, 6, 7]
arr = [2, 3, 5, 7, 1, 4, 6]
permutations = itertools.permutations(arr)

tot = 0
count = 0

# Print each permutation
for perm in permutations:
    tot += 1
    sub = 0
    for p in primes:
        if perm[p - 1] == p:
            sub += 1
    if sub == 3:
        count += 1

print(count)
print(tot)
print(f"prob: {count / tot:.5f}")