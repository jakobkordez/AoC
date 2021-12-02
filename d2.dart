import 'dart:io';

void main() {
  // Part 2
  print(File('i2.txt')
      .readAsLinesSync()
      .map((e) => e.split(' '))
      .map((e) => [e[0], int.parse(e[1])])
      .fold<List<int>>(
        [0, 0, 0],
        (s, c) => c[0] == 'down'
            ? (s..[0] += c[1] as int)
            : c[0] == 'up'
                ? (s..[0] -= c[1] as int)
                : [s[0], s[1] + (c[1] as int), s[2] + s[0] * (c[1] as int)],
      )
      .skip(1)
      .reduce((v, e) => v * e));
}
