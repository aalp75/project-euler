#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>

// #include "debug.h"

using namespace std;

using ll = long long;

const int INF32 = 1e9;

vector<vector<int>> all_sums((int)5e5);

void preprocess() {
}

void show(vector<int>& v) {
    cout << "vector = { ";
    for (auto e : v) {
        cout << e << " ";
    }
    cout << "}\n";
}

void clean_all_sums(vector<int>& v) {
    for (auto e : v) {
        all_sums[e].clear();
    }
}

bool check(vector<int>& a) {

    int n = (int)a.size();
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

        for (auto e : all_sums[s]) {
            if ((e & mask) == 0) { // disjoint subset
                clean_all_sums(cache);
                return false;
            }
        }

        min_sum[l] = min(min_sum[l], s);
        max_sum[l] = max(max_sum[l], s);

        all_sums[s].push_back(mask);
        cache.push_back(s);
    }

    clean_all_sums(cache);

    for (int l = 2; l <= n; l++) {
        if (min_sum[l] <= max_sum[l - 1]) {
            return false;
        }
    }

    return true;
}

void solve() {
    std::ifstream file("inputs/inputs105.txt");
    std::string line;

    std::vector<std::vector<int>> allRows;

    while (std::getline(file, line)) {
        std::vector<int> row;
        std::stringstream ss(line);
        std::string value;

        while (std::getline(ss, value, ',')) {
            row.push_back(std::stoi(value));
        }

        allRows.push_back(row);
    }

    int ans = 0;
    for (const auto& row : allRows) {
        vector<int> v;
        for (int num : row) {
            v.push_back(num);
        }

        if (check(v)) {
            for (auto e : v) {
                ans += e;
            }
        }
    }

    cout << "Solution is " << ans << endl;
    return;
}

int main() {
    preprocess();
    solve();
    return 0;
}