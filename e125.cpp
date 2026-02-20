#include <utility>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
#include <set>

#include "debug.h"

using namespace std;

using ll = long long;

bool isPalindrome(ll x) {
    if (x == 1) return false;
    string s = to_string(x);
    int n = (int)s.size();
    for (int i = 0; i < n; i++) {
        if (s[i] != s[n - 1 - i]) return false;
    }
    return true;
}

void solve() {
    ll lim = 1e8;
    int n = (int)ceil(sqrtl(lim)) + 1;
    set<int> s;

    for (int i = 1; i < n; i++) { // start
        ll cur = 1LL * i * i;
        for (int j = i + 1; j < n; j++) {
            cur += 1LL * j * j;
            if (cur > lim) break;

            if (isPalindrome(cur)) {
                s.insert((int)cur);
            }
        }
    }

    ll ans = accumulate(s.begin(), s.end(), 0ll);
    cout << "Solution: " << ans << " (" << s.size() << " elements)" << "\n";
}

int main() {
    solve();
    return 0;
}