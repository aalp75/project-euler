
#include <bits/stdc++.h>

#ifdef LOG
#include "debug.h"
#else
#define debug(...)
#endif

using namespace std;
typedef long long ll;

ll LIM;

vector<ll> prime_divisor;

// precompute all the prime divisors from 1 to LIM using the sieve of eratosthenes
void precompute_prime_divisors() {
    prime_divisor.resize(LIM + 1, -1);
    vector<bool> is_prime(LIM + 1, true);
    for (int i = 2; i <= LIM; i++) {
        if (!is_prime[i]) continue;
        prime_divisor[i] = i;
        for (int j = 2 * i; j <= LIM; j += i) {
            is_prime[j] = false;
            if (prime_divisor[j] == -1) {
                prime_divisor[j] = i;
            }
        }
    }   
}

// return the prime decomposition of a number x = p1 ^ q1 + p2 ^ q2 + ... + p2 ^ qn
// in the form {{p1, q1}, {p2, q2}, ..., {pn, qn}}
vector<pair<ll, ll>> compute_prime_decomposition(ll x) {
    
    map<int, int> prime_decomposition_map;
    while (prime_divisor[x] > 1) {
        prime_decomposition_map[prime_divisor[x]]++;
        x /= prime_divisor[x];
    }
    vector<pair<ll, ll>> prime_decomposition;
    for (auto keyval : prime_decomposition_map) {
        prime_decomposition.push_back({keyval.first, keyval.second});
    }
    return prime_decomposition;
}

void solve() {

}

int main() {
    LIM = 5e10;
    precompute_prime_divisors();
    solve();
    cout << "Done!" << endl;
    return 0;
}