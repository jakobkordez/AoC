#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <tuple>

using namespace std;

vector<string> d;
int h, w, sx, sy, x, y, ox, oy, dx, dy, result;

void findStart()
{
    for (sy = 0; sy < h; ++sy)
        for (sx = 0; sx < w; ++sx)
            if (d[sy][sx] == '^')
                return;
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

    findStart();

    x = sx;
    y = sy;
    dx = 0;
    dy = -1;
    int p1 = 1;
    while (0 <= x + dx && x + dx < w && 0 <= y + dy && y + dy < h)
    {
        if (d[y + dy][x + dx] == '#')
        {
            swap(dx, dy);
            dx = -dx;
            continue;
        }
        x += dx;
        y += dy;
        if (d[y][x] == '.')
        {
            ++p1;
            d[y][x] = 'X';
        }
    }
    cout << p1 << '\n';

    result = 0;
    for (oy = 0; oy < h; ++oy)
        for (ox = 0; ox < w; ++ox)
        {
            if (d[oy][ox] != 'X')
                continue;
            d[oy][ox] = '#';
            x = sx;
            y = sy;
            dx = 0;
            dy = -1;
            int dir = 0;
            auto cache = new set<int>();
            while (0 <= x + dx && x + dx < w && 0 <= y + dy && y + dy < h)
            {
                if (d[y + dy][x + dx] == '#')
                {
                    swap(dx, dy);
                    dx = -dx;
                    dir = (dir + 1) % 4;
                    continue;
                }
                x += dx;
                y += dy;
                auto tpl = (dir << 16) | (x << 8) | y;
                if (cache->find(tpl) != cache->end())
                {
                    result++;
                    break;
                }
                cache->emplace(tpl);
            }
            d[oy][ox] = 'X';
        }

    cout << result << '\n';

    return 0;
}