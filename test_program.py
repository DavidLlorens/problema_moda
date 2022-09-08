from unittest import TestCase, main
from random import seed, randint
from program import mode


def create_problem(n: int) -> list[int]:
    return [randint(0, min(n, 1000)) for _ in range(n)]


class Test(TestCase):
    def test_mode_1(self):
        self.assertEqual((7, 1), mode([7]))

    def test_mode_2(self):
        self.assertEqual((2, 5), mode([7, 2, 2, 2, 2, 7, 7, 7, 2]))

    def test_mode_3(self):
        self.assertEqual((1, 4), mode([7, 7, 7, 7, 1, 1, 1, 1, 4, 4, 4, 4, 3, 3, 3]))

    def test_mode_4(self):
        seed(42)
        p = create_problem(100000)
        self.assertEqual((102, 139), mode(p))

    def test_mode_5(self):
        seed(42)
        p = create_problem(1000000)
        self.assertEqual((990, 1128), mode(p))


if __name__ == "__main__":
    main()