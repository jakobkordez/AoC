#include <iostream>
#include <vector>
#include <string>

using namespace std;

int p[1000][1000];
int h, w;
vector<string> d;

void reset()
{
    for (int i = 0; i < h; ++i)
        for (int j = 0; j < w; ++j)
            p[i][j] = 0;
}

int go(int x, int y, int dx, int dy)
{
    int c = 0;
    int hsh, t;
    while (true)
    {
        if (x < 0 || x >= h || y < 0 || y >= w)
            break;
        hsh = 1 << ((dx == 0 ? 1 : 0) | (dx + dy > 0 ? 2 : 0));
        if (p[y][x] & hsh)
            break;
        if (p[y][x] == 0)
            ++c;
        p[y][x] |= hsh;
        if (dx != 0 && d[y][x] == '|')
        {
            c += go(x, y + 1, 0, 1);
            c += go(x, y - 1, 0, -1);
            break;
        }
        if (dy != 0 && d[y][x] == '-')
        {
            c += go(x + 1, y, 1, 0);
            c += go(x - 1, y, -1, 0);
            break;
        }
        if (d[y][x] == '\\')
            swap(dx, dy);
        else if (d[y][x] == '/')
        {
            t = -dx;
            dx = -dy;
            dy = t;
        }
        x += dx;
        y += dy;
    }
    return c;
}

int main()
{
    string s;
    while (getline(cin, s))
    {
        d.push_back(s);
    }
    h = d.size();
    w = d[0].size() - 1;

    cout << "Part 1: " << go(0, 0, 1, 0) << endl;

    int mx = 0, t;
    for (int i = 0; i < h; ++i)
    {
        reset();
        t = go(0, i, 1, 0);
        if (t > mx)
            mx = t;
        reset();
        t = go(w - 1, i, -1, 0);
        if (t > mx)
            mx = t;
    }
    for (int i = 0; i < w; ++i)
    {
        reset();
        t = go(i, 0, 0, 1);
        if (t > mx)
            mx = t;
        reset();
        t = go(i, h - 1, 0, -1);
        if (t > mx)
            mx = t;
    }

    cout << "Part 2: " << mx << endl;

    return 0;
}