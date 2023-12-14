#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

vector<string> p;
int H, W;

void roll(int x, int y, int dx, int dy)
{
    int jx = x, jy = y;
    while (0 <= y && y < H && 0 <= x && x < W)
    {
        if (p[y][x] == '.')
        {
            if (dx + dy > 0)
            {
                jx = max(jx, x + dx);
                jy = max(jy, y + dy);
            }
            else
            {
                jx = min(jx, x + dx);
                jy = min(jy, y + dy);
            }
            while (0 <= jy && jy < H && 0 <= jx && jx < W)
            {
                if (p[jy][jx] == '#')
                {
                    x = jx;
                    y = jy;
                    break;
                }
                if (p[jy][jx] == 'O')
                {
                    swap(p[y][x], p[jy][jx]);
                    break;
                }
                jx += dx;
                jy += dy;
            }
        }
        x += dx;
        y += dy;
    }
}

void cycle()
{
    for (int x = 0; x < W; x++)
        roll(x, 0, 0, 1);
    for (int y = 0; y < H; y++)
        roll(0, y, 1, 0);
    for (int x = 0; x < W; x++)
        roll(x, H - 1, 0, -1);
    for (int y = 0; y < H; y++)
        roll(W - 1, y, -1, 0);
}

int calc()
{
    int res = 0;
    for (int y = 0; y < H; y++)
        for (int x = 0; x < W; x++)
            if (p[y][x] == 'O')
                res += H - y;
    return res;
}

int main()
{

    string row;
    while (getline(cin, row))
        p.push_back(row);
    H = p.size();
    W = p[0].size();

    for (int x = 0; x < W; x++)
        roll(x, 0, 0, 1);

    cout << "Part 1: " << calc() << endl;

    int i;
    set<string> seen;
    vector<string> prev;
    vector<int> scores;

    while (true)
    {
        row = "";
        for (i = 0; i < H; i++)
            row += p[i];
        if (seen.find(row) != seen.end())
            break;
        prev.push_back(row);
        seen.insert(row);
        scores.push_back(calc());
        cycle();
    }

    int offset;
    for (offset = 0; offset < prev.size(); offset++)
        if (prev[offset] == row)
            break;
    int repeat = scores.size() - offset;

    cout << "Part 2: " << scores[((1000000000 - offset) % repeat) + offset] << endl;

    return 0;
}