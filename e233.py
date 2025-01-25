# solution is based on "Sum of two squares theorem" and the prime factorization of 420 = 4 * 3 * 5 * 7

from utils import compute_time

P_LIM = 5 * 10 ** 6
COMP_LIM = 10 ** 11 / (5 ** 3 * 13 ** 2 * 17) # smallest solution

def precompute_primes():
    primes = []
    comp = {1}
    is_prime = [True for i in range(P_LIM)]
    for i in range(2, P_LIM):
        if not is_prime[i]:
            continue
        primes.append(i)
        j = 2 * i
        while j < P_LIM:
            is_prime[j] = False
            j += i

    good_primes = []
    bad_primes = []
    for p in primes:
        if p % 4 == 1:
            good_primes.append(p)
        else:
            bad_primes.append(p)
            comp.add(p)

    for i in range(20):
        new_elem = []
        list_mult = list(comp)
        list_mult.sort()
        for mult in list_mult:
            for p in bad_primes:
                k = mult * p
                if k <= COMP_LIM:
                    new_elem.append(k)
                else:
                    break
        for e in new_elem:
            comp.add(e)

    comp = list(comp)
    comp.sort()

    return good_primes, comp

@compute_time
def solve(N):
    good_primes, comp = precompute_primes()
    sol = 0

    #case 1
    d1, d2 = 3, 2
    for p1 in good_primes:
        p1d1 = p1 ** 3
        if p1d1 > N:
            break
        for p2 in good_primes:
            if p2 == p1: 
                continue
            p1d1p2d2 = p1d1 * p2 ** 2
            if p1d1p2d2 > N:
                break
            for p3 in good_primes:
                if p3 == p1 or p3 == p2:
                    continue
                p = p1d1p2d2 * p3
                if p > N:
                    break
                for q in comp:
                    if q * p <= N:
                        sol += p * q
                    else:
                        break

    #case 2
    for d1, d2 in [[7, 3], [10, 2], [17, 1]]:
        for p1 in good_primes:
            p1d1 = p1 ** d1
            if p1d1 > N: 
                break
            for p2 in good_primes:
                if p1 == p2:
                    continue
                p2d2 = p2 ** d2
                p = p1d1 * p2d2
                if p > N:
                    break
                for q in comp:
                    if q * p <= N:
                        sol += p * q
                    else:
                        break

    return sol

if __name__ == "__main__":
    N = 10 ** 11
    sol = solve(N)
    print("Solution: %d" %(sol))
