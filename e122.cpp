#include <utility>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

#include "debug.h"

using namespace std;

using ll = long long;

void solve(int n) {
    vector<int> upper_bounds(n + 1, 0);

    for (int i = 2; i <= n; i++) {
        if (i % 2 == 0) {
            upper_bounds[i] = 1 + upper_bounds[i / 2];
        } else {
            upper_bounds[i] = 1 + upper_bounds[i - 1];
        }
    }

    debug(upper_bounds);

    vector<int> best(upper_bounds);

    auto dfs = [&](auto&& dfs, vector<int> node) -> void {
        int last = node.back();
        int d = (int)node.size() - 1;

        if (d > best[last]) return;

        for (auto e1 : node) {
            for (auto e2 : node) {
                int v = e1 + e2;
                if (v <= last || v > n || d + 1 >= best[v]) continue; // too big

                best[v] = d + 1;

                vector<int> nxt(node);
                nxt.push_back(e1 + e2);
                dfs(dfs, nxt);
            }
        }
    };

    dfs(dfs, {1});

    int ans = 0;
    ans = accumulate(best.begin(), best.end(), 0);
    cout << "Solution: " << ans << "\n";
}

int main() {
    int n = 200;
    solve(n);
    return 0;
}