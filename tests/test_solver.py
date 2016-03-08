import unittest

from solver import solver


class SolverTestCase(unittest.TestCase):

    def test_example1(self):
        """
        Maximise:
            x_1 + x_2

        Subject to:
            4*x_1 - x_2 <= 8
            2*x_1 + x_2 <= 10
            5*x_1 - 2*x_2 >= -2

        Where:
            x_1, x_2 >= 0

        Expected:
            Maximum of 8.00 at x1=2.00, x2=6.00
        """

        tableau = [[0., -1., -1., 0., 0., 0.],
                   [8.,  4., -1., 1., 0., 0.],
                   [10., 2.,  1., 0., 1., 0.],
                   [2., -5.,  2., 0., 0., 1.]]

        result = solver.simplex(tableau)
        sol = solver.get_basic_solution(result)

        self.assertAlmostEqual(result[0][0], 8., 2)
        self.assertAlmostEqual(sol[0], 2., 2)
        self.assertAlmostEqual(sol[1], 6., 2)

    def test_example2(self):
        """
        Maximise:
            40*x_1 + 30*x_2

        Subject to:
            1*x_1 + 2*x_2 <= 16
            1*x_1 + 1*x_2 <= 9
            3*x_1 + 2*x_2 <= 24

        Where:
            x_1, x_2 >= 0

        Expected:
            Maximum of 330.00 at x1=6.00, x2=3.00
        """

        tableau = [[0., -40., -30., 0., 0., 0., 0.],
                   [16., 1., 2., 1., 0., 0., 0.],
                   [9., 1., 1., 0., 1., 0., 0.],
                   [24., 3., 2., 0., 0., 1., 0.]]

        result = solver.simplex(tableau)
        sol = solver.get_basic_solution(result)

        self.assertAlmostEqual(result[0][0], 330., 2)
        self.assertAlmostEqual(sol[0], 6., 2)
        self.assertAlmostEqual(sol[1], 3., 2)

    def test_example3(self):
        """
        Maximise:
            x_1 + x_2

        Subject to:
            2*x_1 + 1*x_2 <= 4
            1*x_1 + 2*x_2 <= 3

        Where:
            x_1, x_2 >= 0

        Expected:
            Maximum of 2.33 at x1=1.67, x2=0.67
        """

        tableau = [[0., -1., -1., 0., 0., 0.],
                   [4., 2., 1., 1., 0., 0.],
                   [3., 1., 2., 0., 1., 0.]]

        result = solver.simplex(tableau)
        sol = solver.get_basic_solution(result)

        self.assertAlmostEqual(result[0][0], 2.33, 2)
        self.assertAlmostEqual(sol[0], 1.67, 2)
        self.assertAlmostEqual(sol[1], 0.67, 2)

    def test_example4(self):
        """
        Maximise:
            4*x_1 + 6*x_2

        Subject to:
            -1*x_1 + 1*x_2 <= 11
            1*x_1 + 1*x_2 <= 27
            2*x_1 + 5*x_2 <= 90

        Where:
            x_1, x_2 >= 0

        Expected:
            Maximum of 132.00 at x1=15.00, x2=12.00
        """

        tableau = [[0., -4., -6., 0., 0., 0.],
                   [11., -1., 1., 1., 0., 0.],
                   [27., 1., 1., 0., 1., 0.],
                   [90., 2., 5., 0., 0., 1.]]

        result = solver.simplex(tableau)
        sol = solver.get_basic_solution(result)

        self.assertAlmostEqual(result[0][0], 132., 2)
        self.assertAlmostEqual(sol[0], 15., 2)
        self.assertAlmostEqual(sol[1], 12., 2)
