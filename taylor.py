import math
from typing import Tuple


def get_actual_value(x: float) -> float:
    """
    Returns actual expected value
    >>> get_actual_value(.6)
    0.8686968577706227
    """
    return math.sin(2 * x) ** 2


def calc_taylor_series(x: float, iters: int):
    """
    Calculates taylor series
    >>> calc_taylor_series(.4, 5)
    0.5145849010793652
    """
    x %= math.pi / 2
    return 0.5 + sum(
        map(lambda k: (-1) ** (k + 1) * (2 ** (4 * k - 1)) / math.factorial(2 * k) * (x ** (2 * k)), range(iters)))


def calc_error(x: float, iters: int):
    """
    >>> calc_error(.56, 6)
    1.620769026267066e-05
    """
    return abs(calc_taylor_series(x, iters) - get_actual_value(x))


def calc_max_error(iters: int) -> float:
    """
    Returns maximum error
    >>> calc_max_error(10)
    0.0017307803078218393
    """
    return max(map(lambda x: calc_error(x / 500, iters), range(int(math.pi * 1000))))


def get_count(x: float, epsilon: int):
    """
    Returns number of elements you need to achieve epsilon accuracy at point x
    >>> get_count(.13, 10 ** -2)
    2
    """
    actual_value = get_actual_value(x)
    x %= math.pi / 2
    value = 0.5
    k = 0
    while abs(value - actual_value) >= epsilon:
        value += (-1) ** (k + 1) * (2 ** (4 * k - 1)) / math.factorial(2 * k) * (x ** (2 * k))
        k += 1
    return k


def taylor_series(x: float, iters: int) -> Tuple[float, float]:
    """

    :param x:
    :param iters:
    :return:
    """
    return calc_error(x, iters), calc_taylor_series(x, iters)


def main():
    pass
