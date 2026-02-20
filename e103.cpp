#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

const int INF32 = 1e9;

ll counter = 0;

int ans = INF32;
vector<int> best_cand;

int min_value = 11;
int max_value = 50;

int n = 7;

vector<bool> all_sums(max_value * n + 1, false);

void preprocess() {
}

void show(vector<int>& v) {
    cout << "vector: ";
    for (auto e : v) {
        cout << e << " ";
    }
    cout << "\n";
}

void clean_all_sums(vector<int>& v) {
    for (auto e : v) {
        all_sums[e] = false;
    }
}

bool check(vector<int>& a) {

    int n = a.size();
    int mask_bound = 1 << n;

    bool good = true;

    vector<int> cache;

    vector<int> min_sum(n + 1, INF32);
    vector<int> max_sum(n + 1, 0);

    for (int mask = 1; mask < mask_bound; mask++) {

        int s = 0;
        int l = 0;

        for (int j = 0; j < n; j++) {
            int p2 = 1 << j;

            if ((mask & p2) == p2) {
                s += a[j];
                l++;
            }
        }

        if (all_sums[s]) { // already exist
            clean_all_sums(cache);
            return false;
        }

        min_sum[l] = min(min_sum[l], s);
        max_sum[l] = max(max_sum[l], s);

        all_sums[s] = true;
        cache.push_back(s);
    }

    clean_all_sums(cache);

    for (int l = 2; l <= n; l++) {
        // any array with 3 elements should be greater than any array with 2 elements
        // less array with 3 elements should be greater than best array with 2 elements

        if (min_sum[l] <= max_sum[l - 1]) {
            return false;
        }
    }

    return true;
}

void build_recur(vector<int>& curr, int index, int curr_min) {

    if (index == n) {
        counter += 1;

        if (check(curr)) {
            int s = 0;
            for (auto e : curr) s += e;

            if (s < ans) {
                ans = s;
                best_cand = curr;
            }
        }
        return;
    }

    for (int v = curr_min; v <= max_value; v++) {
        curr.push_back(v);
        build_recur(curr, index + 1, v + 1);
        curr.pop_back();
    }
}

void solve() {
    vector<int> curr;
    build_recur(curr, 0, min_value);
    cout << "iterations: " << counter << endl;
}

int main() {
    preprocess();
    solve();
    cout << "ans: " << ans << "\n";
    show(best_cand);
    cout << "Done\n";
    return 0;
}