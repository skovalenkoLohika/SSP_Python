from Phase1 import fibonacci
from unittest_data_provider import data_provider


class TestFibonacci():
    data = lambda: (
        (5, [0, 1, 1, 2, 3, 5, 8]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
    )

    @data_provider(data)
    def test_fibonacci(self, num, result):
        test = fibonacci.fib(num)
        assert (result == test)
