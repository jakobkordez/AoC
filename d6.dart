import 'dart:io';

void main() {
  const n = 256;
  BigInt d7 = BigInt.zero, d8 = BigInt.zero, t;
  int i;
  final d = List.filled(7, BigInt.zero);
  File('i6.txt')
      .readAsStringSync()
      .split(',')
      .forEach((e) => d[int.parse(e)] += BigInt.one);

  final sw = Stopwatch();
  sw.start();
  for (i = 0; i < n; ++i) {
    t = d[i % 7];
    d[i % 7] += d7;
    d7 = d8;
    d8 = t;
  }
  sw.stop();

  final res = d.reduce((a, b) => a + b) + d7 + d8;
  print(res);
  print('${res.bitLength} bits');
  print('${sw.elapsedMilliseconds} ms');
}
