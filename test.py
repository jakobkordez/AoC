import unittest
from parameterized import parameterized
import subprocess
import sys
import re
from os import path

partRe = re.compile(r'Part (\d+): (\S+)')


class _Test(unittest.TestCase):
    def __init__(self, year, *args, **kwargs) -> None:
        self.year = year
        super().__init__(*args, **kwargs)

    def _test(self, day, *answers):
        cwd = path.join(path.dirname(__file__), f'{self.year}')
        try:
            output = subprocess.check_output(
                [sys.executable, f'{day}.py'], cwd=cwd, timeout=3)
        except subprocess.TimeoutExpired:
            self.skipTest(f'Timeout on {self.year}/{day}')

        checked = [False] * len(answers)
        for m in partRe.finditer(output.decode()):
            p, r = m.groups()
            p = int(p) - 1
            self.assertEqual(
                r, answers[p], f'Part {p + 1} incorrect on {self.year}/{day}')
            checked[p] = True
        self.assertTrue(
            all(checked), f'Not all parts were outputted on {self.year}/{day}')


class Test2022(_Test):
    def __init__(self, *args, **kwargs):
        super().__init__('2022', *args, **kwargs)

    @parameterized.expand([
        ['d01', '65912', '195625'],
        ['d02', '11906', '11186'],
        ['d03', '7742', '2276'],
        ['d04', '483', '874'],
        ['d05', 'QMBMJDFTD', 'NBTVTJNFJ'],
        ['d06', '1647', '2447'],
        ['d07', '1770595', '2195372'],
        ['d08', '1695', '287040'],
        ['d09', '6266', '2369'],
        ['d10', '13220'],
        ['d11', '58056', '15048718170'],
        ['d12', '484', '478'],
        ['d13', '5588', '23958'],
        ['d14', '817', '23416'],
        ['d15', '4724228', '13622251246513'],
        ['d16', '1845', '2286'],
        ['d17', '3177', '1565517241382'],
        ['d18', '4302', '2492'],
        ['d19', '1023', '13520'],
    ])
    def test(self, day, *answers):
        super()._test(day, *answers)

    def test_d10_part2(self):
        cwd = path.join(path.dirname(__file__), '2022')
        output = subprocess.check_output([sys.executable, 'd10.py'], cwd=cwd)
        output = list(map(str.rstrip, output.decode().splitlines()))

        expected = [
            '# # #     #     #     # #     #     #   #     #   # # #     # # # #   #     #',
            '#     #   #     #   #     #   #   #     #     #   #     #   #         #   #',
            '#     #   #     #   #     #   # #       # # # #   # # #     # # #     # #',
            '# # #     #     #   # # # #   #   #     #     #   #     #   #         #   #',
            '#   #     #     #   #     #   #   #     #     #   #     #   #         #   #',
            '#     #     # #     #     #   #     #   #     #   # # #     # # # #   #     #',
        ]

        for i, line in enumerate(expected):
            self.assertEqual(line, output[i+2],
                             f'Part 2 incorrect on 2022/d10')


@unittest.skip
class Test2021(_Test):
    def __init__(self, *args, **kwargs):
        super().__init__('2021', *args, **kwargs)

    @parameterized.expand([
        ['d01', '1316', '1344'],
        ['d02', '1690020', '1408487760'],
        ['d03', '3148794', '2795310'],
        ['d04', '55770', '2980'],
        ['d05', '6311', '19929'],
        ['d06', '393019', '1757714216975'],
        ['d07', '353800', '98119739'],
        ['d08', '525', '1083859'],
        ['d09', '631', '821560'],
        ['d10', '369105', '3999363569'],
        ['d11', '1652', '220'],
        ['d12', '4659', '148962'],
        ['d13', '653'],
        ['d14', '2549', '2516901104210'],
        ['d15', '696', '2952'],
        ['d16', '977', '101501020883'],
        ['d17', '2278', '996'],
        ['d18', '3551', '4555'],
        ['d19', '372', '12241'],
        ['d20', '5229', '17009'],
        ['d21', '906093', '274291038026362'],
        ['d22', '601104', '1262883317822267'],
        ['d23', '11320', '49532'],
        ['d24', '29991993698469', '14691271141118'],
        ['d25', '295'],
    ])
    def test(self, day, *answers):
        super()._test(day, *answers)

    def test_d13_part2(self):
        cwd = path.join(path.dirname(__file__), '2021')
        output = subprocess.check_output([sys.executable, 'd13.py'], cwd=cwd)
        output = list(map(str.rstrip, output.decode().splitlines()))

        expected = [
            '#         #     #   # # #     # # # #   # # #     # # #     # # #     #     #',
            '#         #   #     #     #   #         #     #   #     #   #     #   #   #',
            '#         # #       #     #   # # #     # # #     #     #   #     #   # #',
            '#         #   #     # # #     #         #     #   # # #     # # #     #   #',
            '#         #   #     #   #     #         #     #   #         #   #     #   #',
            '# # # #   #     #   #     #   # # # #   # # #     #         #     #   #     #',
        ]

        for i, line in enumerate(expected):
            self.assertEqual(line, output[i+2],
                             f'Part 2 incorrect on 2021/d13')


if __name__ == '__main__':
    unittest.main()
