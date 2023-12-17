#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <tuple>

using namespace std;

vector<string> map;
int h, w;

int dxp[4] = {0, 1, 0, -1};
int dyp[4] = {-1, 0, 1, 0};

struct Node
{
    int d, x, y, dr, t;
    Node(int d = 0, int x = 0, int y = 0, int dr = 0, int t = 0) : d(d), x(x), y(y), dr(dr), t(t) {}
    bool operator()(Node const &l, Node const &r) const { return l.d > r.d; }
};

int solve(int max_s, int min_s = 0)
{
    set<tuple<int, int, int>> seen;
    priority_queue<Node, vector<Node>, Node> pq;
    pq.emplace(Node(0, 1, 0, 1));
    pq.emplace(Node(0, 0, 1, 2));

    Node n;
    int d, x, y, dr, t, lft, rgt, dx, dy, dist, fx, fy;
    tuple<int, int, int> tpl;
    while (!pq.empty())
    {
        n = pq.top();
        pq.pop();
        d = n.d;
        x = n.x;
        y = n.y;
        dr = n.dr;
        t = n.t;

        if (x < 0 || x >= w || y < 0 || y >= h)
            continue;
        if (dr == -1)
            return d;
        tpl = make_tuple(x, y, dr);
        if (seen.find(tpl) != seen.end())
            continue;
        seen.insert(tpl);

        dx = dxp[dr];
        dy = dyp[dr];

        for (dist = 1; dist <= max_s; ++dist)
        {
            if (x < 0 || x >= w || y < 0 || y >= h)
                break;
            d += map[y][x] - '0';

            if (dist >= min_s)
            {
                if (x == w - 1 && y == h - 1)
                {
                    pq.emplace(Node(d, x, y, -1));
                    break;
                }
                lft = (dr - 1) % 4;
                fx = dxp[lft];
                fy = dyp[lft];
                pq.emplace(Node(d, x + fx, y + fy, lft));
                rgt = (dr + 1) % 4;
                fx = dxp[rgt];
                fy = dyp[rgt];
                pq.emplace(Node(d, x + fx, y + fy, rgt));
            }

            x += dx;
            y += dy;
        }
    }
    return -1;
}

int main()
{

    string s;
    while (getline(cin, s))
        map.push_back(s);

    h = map.size();
    w = map[0].size() - 1;

    cout << "Part 1: " << solve(3) << endl;
    cout << "Part 2: " << solve(10, 4) << endl;

    return 0;
}