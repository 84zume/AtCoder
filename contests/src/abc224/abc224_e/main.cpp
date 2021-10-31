#include <iostream>
#include <string>
#include <vector>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int64_t H, int64_t W, int N, const std::vector<int64_t> &r, const std::vector<int64_t> &c, const std::vector<int64_t> &a) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t H, W;
    int N;
    std::cin >> H >> W >> N;
    std::vector<int64_t> r(N), c(N), a(N);
    REP (i, N) {
        std::cin >> r[i] >> c[i] >> a[i];
    }
    auto ans = solve(H, W, N, r, c, a);
    REP (i, N) {
        std::cout << ans[i] << '\n';
    }
    return 0;
}
