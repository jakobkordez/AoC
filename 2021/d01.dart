import 'dart:io';

void main() {
  // Part 1
  print(File('i01.txt').readAsLinesSync().map(int.parse).fold<List<num>>(
      [0, double.infinity], (pr, e) => [pr[0] += (pr[1] < e ? 1 : 0), e])[0]);
}
