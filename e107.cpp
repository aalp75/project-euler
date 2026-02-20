#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include "debug.h"

using namespace std;

using ll = long long;

const int INF32 = 1e9 + 100;

int n = 40;

vector<int> linker(n + 1);
vector<int> length(n + 1);

void preprocess() {
    for (int i = 1; i <= n; i++) {
        linker[i] = i;
        length[i] = 1;
    }
}

int find(int a) {
    while (linker[a] != a) {
        a = linker[a];
    }
    return a;
}

void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (length[a] < length[b]) swap(a, b);
    linker[b] = a;
    length[a] += length[b];
}

void solve() {
    //ifstream file("inputs/example107.txt");
    ifstream file("inputs/inputs107.txt");
    string line;

    vector<vector<string>> mat = { {""} };

    while (getline(file, line)) {
        vector<string> row = { "" };
        stringstream ss(line);
        string value;

        while (getline(ss, value, ',')) {
            row.push_back(value);
        }

        mat.push_back(row);
    }

    int total_weight = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (mat[i][j] == "-") continue;
            total_weight += stoi(mat[i][j]);
        }
    }

    debug(total_weight);

    vector<pair<int, pair<int, int>>> edges;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (mat[i][j] == "-") continue;
            edges.push_back({ stoi(mat[i][j]), {i, j} });
        }
    }

    sort(edges.begin(), edges.end());

    int new_weight = 0;

    for (auto edge : edges) {
        int a = edge.second.first;
        int b = edge.second.second;
        int w = edge.first;

        if (find(a) == find(b)) continue;

        unite(a, b);
        new_weight += w;
    }

    debug(new_weight);

    int ans = total_weight - new_weight;
    debug(ans);

    return;
}

int main() {
    preprocess();
    solve();
    return 0;
}