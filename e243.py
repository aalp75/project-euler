# empirically we can see that the answer must be a multiple of a highly composite number
# the first composite number less than the target is 2 x 3 x 5 x ... x 29
# so the answer must be between 2 x 3 x 5 x ... x 23 and 2 x 3 x 5 x ... x 29

def euler_totient(n: int) -> int:
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


p = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23

target = 15499 / 94744

for i in range(1, 30):
    x = p * i
    if euler_totient(x) / (x - 1) < target:
        print(f'{x:,}')
        break