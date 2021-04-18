import unittest

import examen


class TestEquivalencePartitioning(unittest.TestCase):

    def test_calculate(self):
        result = examen.calculate(5, [6, 13, 11, 10, 10])
        self.assertEqual(result, [4, 5, 9, 6, 1])
        result = examen.calculate(6, [6, 13, 11, 10, 11, 12])
        self.assertEqual(result, [8, 3, 5, 8, 4, 3])
        result = examen.calculate(7, [6, 13, 11, 10, 11, 12, 13])
        self.assertEqual(result, [11, 2, 2, 9, 8, 2, 4])
        result = examen.calculate(8, [6, 13, 11, 10, 11, 12, 13, 14])
        self.assertEqual(result, -1)
        result = examen.calculate(5, [1000000929, -10000006, 23123120, 232323111, -9282818220])
        self.assertEqual(result, -1)
        result = examen.calculate(5, [1000000929, 10000006, 23123120, 232323111, 928281822])
        self.assertEqual(result, -1)
        result = examen.calculate(5, [1, 2, 3, 4])
        self.assertEqual(result, -1)
        result = examen.calculate(1, None)
        self.assertEqual(result, -1)
        result = examen.calculate(100050, None)
        self.assertEqual(result, -1)


class TestBoundaryValueAnalysis(unittest.TestCase):

    def test_calculate(self):
        result = examen.calculate(3, None)
        self.assertEqual(result, -1)
        result = examen.calculate(100001, None)
        self.assertEqual(result, -1)
        result = examen.calculate(4, None) # boundry admisibil dar ecuatie neadmisibila
        self.assertEqual(result, -1)
        result = examen.calculate(5, [5, 10, 12, 11, 11]) # boundry admisibil, ecuatie admisibila
        self.assertEqual(result, [2, 2, 8, 9, 3])
        result = examen.calculate(4, [-5000, -100000, -5000, -100000]) # boundry admisibi, ecuatie neadmisibila N11 + S11
        self.assertEqual(result, -1)
        result = examen.calculate(5, [509950000, -900010000, 10950000, 599990000, -999000000])  # boundry admisibi, ecuatie admisibila N11+S11 logic
        self.assertEqual(result, [-1000000000, 9950000, 99990000, 1000000, 500000000])
        result = examen.calculate(4, [-5000, 1999900000, -5000, 1999900000])  # boundry admisibi, ecuatie neadmisibila N11 + S12
        self.assertEqual(result, -1)
        result = examen.calculate(5, [509950000, 1099990000, 10950000, 599990000, 1001000000])  # boundry admisibi, ecuatie admisibila N11 + S12
        self.assertEqual(result, [1000000000, 9950000, 99990000, 1000000, 500000000])
        result = examen.calculate(4, [-5000, -900010001, -5000, -900010001])  # boundry admisibi, ecuatie neadmisibila N11 + S21
        self.assertEqual(result, -1)
        result = examen.calculate(5, [509950000, -900010001, 10950000, 599990000, -999000001])  # boundry admisibi, ecuatie admisibila N11 + S21
        self.assertEqual(result, -1)
        result = examen.calculate(4, [-5000, 1999900001, -5000, 1999900001])  # boundry admisibi, ecuatie neadmisibila N11 + S22
        self.assertEqual(result, -1)
        result = examen.calculate(5, [509950000, 1099990001, 10950000, 599990000, 1001000001])  # boundry admisibi, ecuatie admisibila N11 + S22
        self.assertEqual(result, -1)
        result = examen.calculate(100000, [-5000, -100000, -5000, -100000])  # boundry admisibi, ecuatie neadmisibila N12 + S11
        self.assertEqual(result, -1)
        result = examen.calculate(100000, [-5000, 1999900000, -5000, 1999900000])  # boundry admisibi, ecuatie neadmisibila N12 + S12
        self.assertEqual(result, -1)
        result = examen.calculate(100000, [-5000, -900010001, -5000, -900010001])  # boundry admisibi, ecuatie neadmisibila N12 + S21
        self.assertEqual(result, -1)
        result = examen.calculate(99999, [509950000, -900010001, 10950000, 599990000, -999000001])  # boundry admisibi, ecuatie admisibila N12 + S21
        self.assertEqual(result, -1)
        result = examen.calculate(100000, [-5000, 1999900001, -5000, 1999900001])  # boundry admisibi, ecuatie neadmisibila N12 + S22
        self.assertEqual(result, -1)
        result = examen.calculate(99999, [509950000, 1099990001, 10950000, 599990000, 1001000001])  # boundry admisibi, ecuatie admisibila N12 + S22
        self.assertEqual(result, -1)


class TestCategoryPartitioning(unittest.TestCase):

    def test_calculate(self):
        result = examen.calculate(-6, None)# n<3
        self.assertEqual(result, -1)
        result = examen.calculate(3, None)# n=3
        self.assertEqual(result, -1)
        result = examen.calculate(4, None)  # n=4
        self.assertEqual(result, -1)
        result = examen.calculate(5, [6, 13, 11, 10, 11])  # n=5, len(s) = n
        self.assertEqual(result, [5, 4, 8, 6, 2])
        result = examen.calculate(5, [6, 13, 11, 10])  # n=5, len(s) != n
        self.assertEqual(result, -1)
        result = examen.calculate(99999, None)  # n=99999 Caz exceptional (nu se poate testa) la fel si pentru n=100000
        self.assertEqual(result, -1)
        result = examen.calculate(100001, None)  # n=100001
        self.assertEqual(result, -1)
        result = examen.calculate(100005, None)  # n>100001
        self.assertEqual(result, -1)


class TestStatementCoverage(unittest.TestCase):

    def test_calculate(self):
        # result = examen.calculate(None, None)  #intra pe toate inafara de 12-28, 33-34, 37-47
        # self.assertEqual(result, [11, 2, 2, 9, 8, 2, 4])# 6 13 11 10 11 12 13
        result = examen.calculate(3, None)  # nu intra pe 8-27, se opreste la 38
        self.assertEqual(result, -1)
        result = examen.calculate(4, None)
        self.assertEqual(result, -1)
        result = examen.calculate(5, [6, 13, 11, 10, 10])
        self.assertEqual(result, [4, 5, 9, 6, 1])
        result = examen.calculate(6, [6, 13, 11, 10, 11, 12])
        self.assertEqual(result, [8, 3, 5, 8, 4, 3])
        result = examen.calculate(7, [6, 13, 11, 10, 11, 12, 13])
        self.assertEqual(result, [11, 2, 2, 9, 8, 2, 4])
        result = examen.calculate(8, [6, 13, 11, 10, 11, 12, 13, 14])
        self.assertEqual(result, -1)
        result = examen.calculate(5, [1, 2, 3, 4])
        self.assertEqual(result, -1)


class TestBranchCoverage(unittest.TestCase):

    def test_calculate(self):
        result = examen.calculate(4, None)
        self.assertEqual(result, -1)
        result = examen.calculate(8, None)
        self.assertEqual(result, -1)
        result = examen.calculate(2, None)
        self.assertEqual(result, -1)
        result = examen.calculate(5, [6, 13, 11, 10, 10])
        self.assertEqual(result, [4, 5, 9, 6, 1])
        result = examen.calculate(4, [6, 13, 11, 10, 10])
        self.assertEqual(result, -1)


class TestConditionCoverage(unittest.TestCase):

    def test_calculate(self):
        result = examen.calculate(4, None)
        self.assertEqual(result, -1)
        result = examen.calculate(8, None)
        self.assertEqual(result, -1)
        result = examen.calculate(2, None)
        self.assertEqual(result, -1)
        result = examen.calculate(5, [6, 13, 11, 10, 10])
        self.assertEqual(result, [4, 5, 9, 6, 1])
        result = examen.calculate(4, [6, 13, 11, 10, 10])
        self.assertEqual(result, -1)
        result = examen.calculate(100001, None)
        self.assertEqual(result, -1)
        result = examen.calculate(5, [509950000, 1099990000, 10950000, 599990000, 1001000000])
        self.assertEqual(result, [1000000000, 9950000, 99990000, 1000000, 500000000])


class TestCircuitsCoverage(unittest.TestCase):

    def test_calculate(self):
        # result = examen.calculate(None, None)
        # self.assertEqual(result, [11, 2, 2, 9, 8, 2, 4])
        result = examen.calculate(3, None)
        self.assertEqual(result, -1)
        result = examen.calculate(4, [6, 13, 11, 10, 10])
        self.assertEqual(result, -1)
        result = examen.calculate(5, [6, 13, 11, 10, 10])
        self.assertEqual(result, [4, 5, 9, 6, 1])
        result = examen.calculate(6, [6, 13, 11, 10, 11, 12])
        self.assertEqual(result, [8, 3, 5, 8, 4, 3])
        result = examen.calculate(7, [6, 13, 11, 10, 11, 12, 13])
        self.assertEqual(result, [11, 2, 2, 9, 8, 2, 4])
        result = examen.calculate(4, [1, 2, 3, 4])
        self.assertEqual(result, -1)
        result = examen.calculate(5, [509950000, -900010001, 10950000, 599990000, -999000001])
        self.assertEqual(result, -1)
