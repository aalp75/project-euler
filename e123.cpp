#include <utility>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

#include "debug.h"

using namespace std;

using ll = long long;

void solve() {

    ll N = 1e6;
    vector<ll> primes = {1};
    vector<bool> is_prime(N, true);

    for (ll i = 2; i < N; i++) {
        if (!is_prime[i]) continue;
        primes.push_back(i);
        for (ll j = 2 * i; j < N; j += i) {
            is_prime[j] = false;
        }
    }

    debug(primes.size());

    ll lim = 1e10;

    for (ll n = 1; n < (ll)primes.size(); n++) {
        if (n % 2 == 1) {
            ll v = 2 * n * primes[n];
            if (v >= lim) {
                cout << "Solution: " << n << "\n";
                return;
            }
        }
    }

    cout << "No solution found\n";
}

int main() {
    solve();
    return 0;
}