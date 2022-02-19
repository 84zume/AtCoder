#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int N, int Q, const std::vector<int64_t> &a, const std::vector<int64_t> &x, const std::vector<int64_t> &k) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N, Q;
    std::cin >> N;
    std::vector<int64_t> a(N);
    std::cin >> Q;
    std::vector<int64_t> x(Q), k(Q);
    REP (i, N) {
        std::cin >> a[i];
    }
    REP (i, Q) {
        std::cin >> x[i] >> k[i];
    }
    auto ans = solve(N, Q, a, x, k);
    std::cout << c << '\n';
    REP (i, Q) {
        std::cout << e[i] << '\n';
    }
    return 0;
}
