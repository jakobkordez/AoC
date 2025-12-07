import unittest
from parameterized import parameterized
import subprocess
import sys
import re
from os import path

partRe = re.compile(r"Part (\d+): (\S+)")


class _Test(unittest.TestCase):
    def __init__(self, year, *args, **kwargs) -> None:
        self.year = year
        super().__init__(*args, **kwargs)

    def _test(self, day, *answers):
        cwd = path.join(path.dirname(__file__), f"{self.year}")
        try:
            output = subprocess.check_output(
                [sys.executable, f"{day}.py"], cwd=cwd, timeout=5
            )
        except subprocess.TimeoutExpired:
            self.skipTest(f"Timeout on {self.year}/{day}")

        checked = [False] * len(answers)
        for m in partRe.finditer(output.decode()):
            p, r = m.groups()
            p = int(p) - 1
            self.assertEqual(
                r, answers[p], f"Part {p + 1} incorrect on {self.year}/{day}"
            )
            checked[p] = True
        self.assertTrue(
            all(checked), f"Not all parts were outputted on {self.year}/{day}"
        )


class Test2025(_Test):
    def __init__(self, *args, **kwargs):
        super().__init__("2025", *args, **kwargs)

    @parameterized.expand(
        [
            ["d01", "1172", "6932"],
            ["d02", "29818212493", "37432260594"],
            ["d03", "17554", "175053592950232"],
            ["d04", "1384", "8013"],
            ["d05", "811", "338189277144473"],
            ["d06", "7644505810277", "12841228084455"],
            ["d07", "1537", "18818811755665"],
        ]
    )
    def test(self, day, *answers):
        super()._test(day, *answers)


@unittest.skip
class Test2024(_Test):
    def __init__(self, *args, **kwargs):
        super().__init__("2024", *args, **kwargs)

    @parameterized.expand(
        [
            ["d01", "2904518", "18650129"],
            ["d02", "483", "528"],
            ["d03", "183380722", "82733683"],
            ["d04", "2642", "1974"],
            ["d05", "4689", "6336"],
            ["d06", "4647", "1723"],
            ["d07", "303876485655", "146111650210682"],
            ["d08", "214", "809"],
            ["d09", "6401092019345", "6431472344710"],
            ["d10", "667", "1344"],
            ["d11", "229043", "272673043446478"],
            ["d12", "1381056", "834828"],
            ["d13", "26599", "106228669504887"],
            ["d14", "218619120", "7055"],
            ["d15", "1517819", "1538862"],
            ["d16", "91464", "494"],
            ["d17", "4,1,7,6,4,1,0,2,7", "164279024971453"],
            ["d18", "372", "25,6"],
            ["d19", "293", "623924810770264"],
            ["d20", "1327", "985737"],
            ["d21", "197560", "242337182910752"],
            ["d22", "16299144133", "1896"],
            ["d23", "1230", "az,cj,kp,lm,lt,nj,rf,rx,sn,ty,ui,wp,zo"],
            ["d24", "41324968993486", "bmn,jss,mvb,rds,wss,z08,z18,z23"],
            ["d25", "3269"],
        ]
    )
    def test(self, day, *answers):
        super()._test(day, *answers)


@unittest.skip
class Test2023(_Test):
    def __init__(self, *args, **kwargs):
        super().__init__("2023", *args, **kwargs)

    @parameterized.expand(
        [
            ["d01", "55621", "53592"],
            ["d02", "2377", "71220"],
            ["d03", "546563", "91031374"],
            ["d04", "28538", "9425061"],
            ["d05", "379811651", "27992443"],
            ["d06", "861300", "28101347"],
            ["d07", "250370104", "251735672"],
            ["d08", "14429", "10921547990923"],
            ["d09", "1955513104", "1131"],
            ["d10", "6599", "477"],
            ["d11", "9214785", "613686987427"],
            ["d12", "8022", "4968620679637"],
            ["d13", "31877", "42996"],
            ["d14", "112048", "105606"],
            ["d15", "511416", "290779"],
            ["d16", "6816", "8163"],
            ["d17", "755", "881"],
            ["d18", "47045", "147839570293376"],
            ["d19", "377025", "135506683246673"],
            ["d20", "818649769", "246313604784977"],
            ["d21", "3699", "613391294577878"],
            ["d22", "413", "41610"],
            ["d23", "2214", "6594"],
            ["d24", "14046", "808107741406756"],
            ["d25", "569904"],
        ]
    )
    def test(self, day, *answers):
        super()._test(day, *answers)


@unittest.skip
class Test2022(_Test):
    def __init__(self, *args, **kwargs):
        super().__init__("2022", *args, **kwargs)

    @parameterized.expand(
        [
            ["d01", "65912", "195625"],
            ["d02", "11906", "11186"],
            ["d03", "7742", "2276"],
            ["d04", "483", "874"],
            ["d05", "QMBMJDFTD", "NBTVTJNFJ"],
            ["d06", "1647", "2447"],
            ["d07", "1770595", "2195372"],
            ["d08", "1695", "287040"],
            ["d09", "6266", "2369"],
            ["d10", "13220"],
            ["d11", "58056", "15048718170"],
            ["d12", "484", "478"],
            ["d13", "5588", "23958"],
            ["d14", "817", "23416"],
            ["d15", "4724228", "13622251246513"],
            ["d16", "1845", "2286"],
            ["d17", "3177", "1565517241382"],
            ["d18", "4302", "2492"],
            ["d19", "1023", "13520"],
            ["d20", "16533", "4789999181006"],
            ["d21", "160274622817992", "3087390115721"],
            ["d22", "77318", "126017"],
            ["d23", "4000", "1040"],
            ["d24", "277", "877"],
            ["d25", "2-==10===-12=2-1=-=0"],
        ]
    )
    def test(self, day, *answers):
        super()._test(day, *answers)

    def test_d10_part2(self):
        cwd = path.join(path.dirname(__file__), "2022")
        output = subprocess.check_output([sys.executable, "d10.py"], cwd=cwd)
        output = list(map(str.rstrip, output.decode().splitlines()))

        expected = [
            "# # #     #     #     # #     #     #   #     #   # # #     # # # #   #     #",
            "#     #   #     #   #     #   #   #     #     #   #     #   #         #   #",
            "#     #   #     #   #     #   # #       # # # #   # # #     # # #     # #",
            "# # #     #     #   # # # #   #   #     #     #   #     #   #         #   #",
            "#   #     #     #   #     #   #   #     #     #   #     #   #         #   #",
            "#     #     # #     #     #   #     #   #     #   # # #     # # # #   #     #",
        ]

        for i, line in enumerate(expected):
            self.assertEqual(line, output[i + 2], f"Part 2 incorrect on 2022/d10")


@unittest.skip
class Test2021(_Test):
    def __init__(self, *args, **kwargs):
        super().__init__("2021", *args, **kwargs)

    @parameterized.expand(
        [
            ["d01", "1316", "1344"],
            ["d02", "1690020", "1408487760"],
            ["d03", "3148794", "2795310"],
            ["d04", "55770", "2980"],
            ["d05", "6311", "19929"],
            ["d06", "393019", "1757714216975"],
            ["d07", "353800", "98119739"],
            ["d08", "525", "1083859"],
            ["d09", "631", "821560"],
            ["d10", "369105", "3999363569"],
            ["d11", "1652", "220"],
            ["d12", "4659", "148962"],
            ["d13", "653"],
            ["d14", "2549", "2516901104210"],
            ["d15", "696", "2952"],
            ["d16", "977", "101501020883"],
            ["d17", "2278", "996"],
            ["d18", "3551", "4555"],
            ["d19", "372", "12241"],
            ["d20", "5229", "17009"],
            ["d21", "906093", "274291038026362"],
            ["d22", "601104", "1262883317822267"],
            ["d23", "11320", "49532"],
            ["d24", "29991993698469", "14691271141118"],
            ["d25", "295"],
        ]
    )
    def test(self, day, *answers):
        super()._test(day, *answers)

    def test_d13_part2(self):
        cwd = path.join(path.dirname(__file__), "2021")
        output = subprocess.check_output([sys.executable, "d13.py"], cwd=cwd)
        output = list(map(str.rstrip, output.decode().splitlines()))

        expected = [
            "#         #     #   # # #     # # # #   # # #     # # #     # # #     #     #",
            "#         #   #     #     #   #         #     #   #     #   #     #   #   #",
            "#         # #       #     #   # # #     # # #     #     #   #     #   # #",
            "#         #   #     # # #     #         #     #   # # #     # # #     #   #",
            "#         #   #     #   #     #         #     #   #         #   #     #   #",
            "# # # #   #     #   #     #   # # # #   # # #     #         #     #   #     #",
        ]

        for i, line in enumerate(expected):
            self.assertEqual(line, output[i + 2], f"Part 2 incorrect on 2021/d13")


if __name__ == "__main__":
    unittest.main()
