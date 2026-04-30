
#include <bits/stdc++.h>

#ifdef LOG
#include "debug.h"
#else
#define debug(...)
#endif

using namespace std;
typedef long long ll;

/**
 * Brute force approach. Generate all primes with the sieve up to 1e7
 * For each prime, check wether its square verify the 2 conditions:
 *  1. It is not a palindrome
 *  2. Its reverse is also the square of a prime
 */

// check if x is a palindrome number
bool checkPalindrome(long long x) {
    string s = to_string(x);
    string t = s;
    reverse(t.begin(), t.end());
    return s == t;
}

ll reverseNumber(long long x) {
    string s = to_string(x);
    reverse(s.begin(), s.end());
    return stoll(s);
}

void solve() {
    const int N = 1e8;
    vector<ll> primes;
    vector<bool> isPrime(N, true);
    for (ll i = 2; i < N; i++) {
        if (!isPrime[i]) continue;
        primes.push_back(i);
        for (ll j = i * i; j < N; j += i) {
            isPrime[j] = false;
        }
    }

    vector<ll> reversiblePrimes;

    for (auto p : primes) {
        ll square = p * p;
        if (checkPalindrome(square)) continue;
        ll rev = reverseNumber(square);

        // find by binary search if it's the square of a prime

        int l = 0;
        int r = primes.size();

        while (l < r) {
            int mid = (l + r) / 2;
            if (primes[mid] * primes[mid] < rev) {
                l = mid + 1;
            }
            else {
                r = mid;
            }
        }

        if (l < primes.size() && primes[l] * primes[l] == rev) {
            reversiblePrimes.push_back(square);

            if ((int)reversiblePrimes.size() == 50) break;
        }
    }
    
    sort(reversiblePrimes.begin(), reversiblePrimes.end());

    debug(reversiblePrimes.size());
    debug(reversiblePrimes);

    ll ans = accumulate(reversiblePrimes.begin(), reversiblePrimes.end(), 0ll);
    
    cout << "Solution: " << ans << '\n';
}

int main() {
    solve();
    cout << "Done!" << endl;
    return 0;
}