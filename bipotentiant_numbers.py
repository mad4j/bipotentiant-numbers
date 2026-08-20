"""Utilities for working with bipotentiant numbers."""

from __future__ import annotations

from typing import List
import sys


def digit_powers(n: int) -> List[int]:
    """Return each digit power used in the bipotentiant definition."""
    if n <= 0:
        raise ValueError("n must be a positive integer")

    return [digit ** exponent for exponent, digit in enumerate(map(int, reversed(str(n))), start=1)]


def is_bipotentiant(n: int) -> bool:
    """Return whether n is bipotentiant."""
    powers = digit_powers(n)
    total = sum(powers)

    product = 1
    for value in powers:
        product *= value

    return n == total + product


def find_bipotentiant_numbers(limit: int) -> List[int]:
    """Return all bipotentiant numbers from 1 through limit inclusive."""
    if limit < 1:
        return []

    return [n for n in range(1, limit + 1) if is_bipotentiant(n)]


def main(argv: List[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    limit = int(args[0]) if args else 1000

    for number in find_bipotentiant_numbers(limit):
        print(number)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
