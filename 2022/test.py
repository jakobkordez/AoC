import unittest
from parameterized import parameterized
import subprocess
import sys
import re

partRe = re.compile(r'Part (\d+): (\S+)')


class Test(unittest.TestCase):
    @parameterized.expand([
        ['d01.py', '65912', '195625'],
        ['d02.py', '11906', '11186'],
        ['d03.py', '7742', '2276'],
        ['d04.py', '483', '874'],
        ['d05.py', 'QMBMJDFTD', 'NBTVTJNFJ'],
        ['d06.py', '1647', '2447'],
        ['d07.py', '1770595', '2195372'],
    ])
    def test(self, day, *answers):
        output = subprocess.check_output([sys.executable, day])
        checked = [False] * len(answers)
        for m in partRe.finditer(output.decode()):
            p, r = m.groups()
            self.assertEqual(r, answers[int(p) - 1],
                             f'Part {p} incorrect on {day}')
            checked[int(p) - 1] = True
        self.assertTrue(all(checked), f'Not all parts were outputted on {day}')


if __name__ == '__main__':
    unittest.main()
