#include <utility>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

#include "debug.h"

using namespace std;

using ll = long long;

const int N = 1e5;

vector<int> primes;
vector<int> prime_factors(N + 1, 1);

void prime_factor_sieve() {
    vector<bool> is_prime(N + 1, true);

    for (int i = 2; i <= N; i++) {
        if (!is_prime[i]) continue;

        primes.push_back(i);
        prime_factors[i] = i;

        for (int j = 2 * i; j <= N; j += i) {
            is_prime[j] = false;
            if (prime_factors[j] == 1)
                prime_factors[j] = i;
        }
    }
}

void solve() {
    // debug(primes);

    vector<pair<int, int>> E = { {0, 0} };

    for (int i = 1; i <= N; i++) {
        ll v = i;
        ll rad = 1;

        while (v > 1) {
            int p = prime_factors[v];
            rad *= p;
            while (v % p == 0)
                v /= p;
        }

        E.push_back({ (int)rad, i });
    }

    sort(E.begin(), E.end());

    // debug(E);

    cout << "Solution: " << E[10000].second << "\n";
}

int main() {
    prime_factor_sieve();
    solve();
    return 0;
}