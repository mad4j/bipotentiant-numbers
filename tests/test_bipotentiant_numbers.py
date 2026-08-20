import unittest
from contextlib import redirect_stdout
from io import StringIO

from bipotentiant_numbers import digit_powers, find_bipotentiant_numbers, is_bipotentiant, main


class BipotentiantNumbersTest(unittest.TestCase):
    def test_digit_powers_follow_right_to_left_exponents(self) -> None:
        self.assertEqual(digit_powers(19), [9, 1])
        self.assertEqual(digit_powers(248), [8, 16, 8])

    def test_raises_for_non_positive_values(self) -> None:
        with self.assertRaises(ValueError):
            digit_powers(0)
        with self.assertRaises(ValueError):
            digit_powers(-1)

    def test_identifies_bipotentiant_numbers(self) -> None:
        self.assertTrue(is_bipotentiant(19))
        self.assertTrue(is_bipotentiant(24))
        self.assertTrue(is_bipotentiant(51))
        self.assertFalse(is_bipotentiant(-1))
        self.assertFalse(is_bipotentiant(0))
        self.assertFalse(is_bipotentiant(20))

    def test_finds_numbers_up_to_limit(self) -> None:
        self.assertEqual(find_bipotentiant_numbers(100), [19, 24, 51])
        self.assertEqual(find_bipotentiant_numbers(0), [])

    def test_main_prints_numbers_up_to_limit(self) -> None:
        stdout = StringIO()

        with redirect_stdout(stdout):
            self.assertEqual(main(["100"]), 0)

        self.assertEqual(stdout.getvalue(), "19\n24\n51\n")


if __name__ == "__main__":
    unittest.main()
