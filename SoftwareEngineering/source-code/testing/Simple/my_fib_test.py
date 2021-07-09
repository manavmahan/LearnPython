import unittest
from my_fib import fib

class Test(unittest.TestCase):
    def test_first(self):
        ex = [1, 1, 2, 3, 5, 8, 14, 21]
        fi = fib()
        for i in ex:
            with self.subTest(i=i):
                a = next(fi)
                self.assertEqual(i, a)

if __name__ == "__main.py__":
    unittest.main()