#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int64_t mm[14];
int64_t p[14][3];

string _go(int i, uint64_t z, uint64_t w, bool dir)
{
    uint64_t x = z % 26 + p[i][1] != w ? 1 : 0;
    z /= p[i][0];
    z *= 25 * x + 1;
    z += (w + p[i][2]) * x;
    if (z >= mm[i])
    {
        return "";
    }
    if (i == 13)
    {
        return "" + to_string(w);
    }
    string r;
    if (dir)
    {
        for (int nw = 1; nw <= 9; ++nw)
        {
            r = _go(i + 1, z, nw, dir);
            if (r != "")
            {
                return "" + to_string(w) + r;
            }
        }
    }
    else
    {
        for (int nw = 9; nw >= 1; --nw)
        {
            r = _go(i + 1, z, nw, dir);
            if (r != "")
            {
                return "" + to_string(w) + r;
            }
        }
    }
    return "";
}

string go(bool dir)
{
    string r;
    if (dir)
    {
        for (int w = 1; w <= 9; ++w)
        {
            r = _go(0, 0, w, dir);
            if (r != "")
            {
                return r;
            }
        }
    }
    else
    {
        for (int w = 9; w >= 1; --w)
        {
            r = _go(0, 0, w, dir);
            if (r != "")
            {
                return r;
            }
        }
    }
    return "";
}

int main()
{

    ifstream cin("i24.txt");
    string sa[14 * 18], t;
    for (int i = 0; i < 14 * 18; ++i)
    {
        getline(cin, sa[i]);
    }

    int j;
    for (int i = 0; i < 14; ++i)
    {
        t = sa[18 * i + 4];
        j = t.find_last_of(' ');
        p[i][0] = stoi(t.substr(j + 1));

        t = sa[18 * i + 5];
        j = t.find_last_of(' ');
        p[i][1] = stoi(t.substr(j + 1));

        t = sa[18 * i + 15];
        j = t.find_last_of(' ');
        p[i][2] = stoi(t.substr(j + 1));
    }

    mm[13] = 1;
    for (int i = 12; i >= 0; --i)
    {
        mm[i] = mm[i + 1] * p[i + 1][0];
    }

    cout << "Part 1: " << go(false) << '\n';
    cout << "Part 2: " << go(true) << '\n';

    return 0;
}