import unittest
from Dice import Dice


class TestDiceMethods(unittest.TestCase):

    def test_dice_equation_dice(self):
        """
        Test for the Dice (Dice.py) class dealing with dice values falling between their set ranges.
        :return: None
        """
        d3 = Dice("1d3")
        d4 = Dice("1d4")
        d6 = Dice("1d6")
        d8 = Dice("1d8")
        d10 = Dice("1d10")
        d12 = Dice("1d12")
        d20 = Dice("1d20")
        d100 = Dice("1d100")

        for i in range(0, 10000):
            self.assertLessEqual(d3.eval(), 3, "d3 is greater than 3")
            self.assertLessEqual(d4.eval(), 4, "d4 is greater than 4")
            self.assertLessEqual(d6.eval(), 6, "d6 is greater than 6")
            self.assertLessEqual(d8.eval(), 8, "d8 is greater than 8")
            self.assertLessEqual(d10.eval(), 10, "d10 is greater than 10")
            self.assertLessEqual(d12.eval(), 12, "d12 is greater than 12")
            self.assertLessEqual(d20.eval(), 20, "d20 is greater than 20")
            self.assertLessEqual(d100.eval(), 100, "d100 is greater than 100")

            self.assertGreaterEqual(d3.eval(), 1, "d3 is less than 1")
            self.assertGreaterEqual(d4.eval(), 1, "d4 is less than 1")
            self.assertGreaterEqual(d6.eval(), 1, "d6 is less than 1")
            self.assertGreaterEqual(d8.eval(), 1, "d8 is less than 1")
            self.assertGreaterEqual(d10.eval(), 1, "d10 is less than 1")
            self.assertGreaterEqual(d12.eval(), 1, "d12 is less than 1")
            self.assertGreaterEqual(d20.eval(), 1, "d20 is less than 1")
            self.assertGreaterEqual(d100.eval(), 1, "d100 is less than 1")

    def test_dice_equation_number(self):
        """
        Test for the Dice (Dice.py) class dealing with singular numbers (negative and positive, including 0).
        :return: None
        """
        for i in range(-10000, 10000):
            self.assertEqual(Dice(str(i)).eval(), i)

    def test_dice_equation_basic_arith(self):
        """
        Test for the Dice (Dice.py) class dealing with single arithmetic operations.
        :return: None
        """
        for i in range(-100, 100):
            for j in range(-100, 100):
                self.assertEqual(Dice(str(i) + "+" + str(j)).eval(), i + j)

    def test_dice_equation_basic_arith_dice(self):

        for i in range(-100, 100):
            d4 = Dice("1d4+" + str(i))
            self.assertLessEqual(d4.eval(), 4 + i)
            self.assertGreaterEqual(d4.eval(), 1 + i)


if __name__ == '__main__':
    unittest.main()
