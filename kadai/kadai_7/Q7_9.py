"""
Q7.9 Answer.
"""
import re
import unittest


def overlap(strA: str, strB: str) -> str:
    ptrA = 0

    while len(strA) > ptrA:
        if strA[ptrA] == strB[0] and re.search(fr"^{strA[ptrA:]}.*", strB) is not None:
            return strA[:ptrA] + strB
        ptrA += 1
    return strA + strB


class OverlapTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual("commummy", overlap("commu", "mummy"))

    def testcase2(self):
        self.assertEqual("boxokxbox", overlap("boxok", "xbox"))

    def testcase3(self):
        self.assertEqual("detery", overlap("deter", "detery"))

    def testcase4(self):
        self.assertEqual("waycomget", overlap("waycom", "ycomget"))

    def testcase5(self):
        self.assertEqual("tttttt", overlap("tttttt", "tttttt"))


if __name__ == '__main__':
    unittest.main()
