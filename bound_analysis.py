"""Bound analysis and extended exhaustive search for bipotentiant numbers.

This module implements the analytical tools developed to prove (or narrow) the
claim that the only base-10 bipotentiant numbers are {0, 19, 24, 51, 1343, 1721}.

Three complementary approaches are implemented:

1. **Bound analysis** – computes max_S(k), max_P(k), max_B(k) for each digit
   count k, allowing a first assessment of how quickly the feasibility window
   closes.

2. **Pruned exhaustive search** – for a k-digit candidate n the product
   P(n) = ∏ dⱼ^(j+1) must satisfy P(n) < 10^k (since P(n) = n − S(n) < n).
   The search exploits this constraint to prune the digit-tuple space,
   reducing the search dramatically compared with a naive scan.

3. **One-non-1-digit analytical lemma** – a closed-form argument that shows
   no k-digit bipotentiant with exactly one digit ≥ 2 exists for k ≥ 28.

Usage::

    python bound_analysis.py            # runs all analyses
    python bound_analysis.py --search   # pruned search only (k=2..14)
    python bound_analysis.py --bounds   # bound table only
    python bound_analysis.py --lemma    # one-non-1-digit lemma only
"""

from __future__ import annotations

import argparse
import math
import time
from typing import List


# ---------------------------------------------------------------------------
# 1. Bound analysis
# ---------------------------------------------------------------------------

def max_S(k: int) -> int:
    """Maximum of S(n) over all k-digit digit-tuples (digits in {1..9}).

    S(n) = Σ dⱼ^(j+1) is maximised when every digit equals 9::

        max_S(k) = Σⱼ₌₀^{k-1} 9^(j+1) = 9·(9^k − 1)/8.
    """
    return 9 * (9**k - 1) // 8


def max_P(k: int) -> int:
    """Maximum of P(n) over all k-digit digit-tuples (digits in {1..9}).

    P(n) = ∏ dⱼ^(j+1) is maximised when every digit equals 9::

        max_P(k) = ∏ⱼ₌₀^{k-1} 9^(j+1) = 9^{k(k+1)/2}.
    """
    return 9 ** (k * (k + 1) // 2)


def print_bound_table(k_max: int = 20) -> None:
    """Print a table of bound values for digit counts k = 1 .. k_max."""
    header = (
        f"{'k':>3}  {'log10(max_S)':>14}  {'log10(max_P)':>14}"
        f"  {'log10(max_B)':>14}  {'log10(10^(k-1))':>16}"
        f"  {'max_B < 10^k':>13}"
    )
    print(header)
    print("-" * len(header))
    for k in range(1, k_max + 1):
        ms = max_S(k)
        mp = max_P(k)
        mb = ms + mp
        log_ms = math.log10(ms)
        log_mp = math.log10(mp)
        log_mb = math.log10(mb)
        lt_maxn = mb < 10**k
        print(
            f"{k:>3}  {log_ms:>14.3f}  {log_mp:>14.3f}"
            f"  {log_mb:>14.3f}  {k - 1:>16}"
            f"  {str(lt_maxn):>13}"
        )


# ---------------------------------------------------------------------------
# 2. Pruned exhaustive search
# ---------------------------------------------------------------------------

def find_bipotentiant_k_digits(k: int) -> List[int]:
    """Return all k-digit bipotentiant numbers via product-pruned search.

    For a k-digit bipotentiant n we must have P(n) < n < 10^k. The search
    tree is pruned as soon as the running product reaches 10^k, which reduces
    the effective branching factor dramatically for large k.
    """
    results: List[int] = []
    limit_P = 10**k
    pow10 = [10**j for j in range(k)]

    def rec(j: int, prod: int, S: int, n_val: int) -> None:
        if j == k:
            if S + prod == n_val:
                results.append(n_val)
            return
        exp = j + 1
        for d in range(1, 10):
            d_pow = d**exp
            new_prod = prod * d_pow
            if new_prod >= limit_P:
                break  # larger d makes the product larger → safe to break
            rec(j + 1, new_prod, S + d_pow, n_val + d * pow10[j])

    rec(0, 1, 0, 0)
    return sorted(results)


def run_pruned_search(k_min: int = 2, k_max: int = 14) -> None:
    """Run the pruned exhaustive search for k = k_min .. k_max and print results."""
    print(f"{'k':>3}  {'Results':>30}  {'Time (s)':>10}")
    total = 0.0
    for k in range(k_min, k_max + 1):
        t0 = time.perf_counter()
        r = find_bipotentiant_k_digits(k)
        elapsed = time.perf_counter() - t0
        total += elapsed
        print(f"{k:>3}  {str(r):>30}  {elapsed:>10.4f}")
    print(f"\nTotal: {total:.2f} s")


# ---------------------------------------------------------------------------
# 3. One-non-1-digit lemma
# ---------------------------------------------------------------------------

def one_non1_lemma_table(k_max: int = 35) -> None:
    """Print the ratio (10^k−1)/9  vs  (k−1)+2·9^k for each k.

    When the ratio exceeds 1, the 'one non-1 digit' fixed-point equation
    has no solution (Lemma 5.1 in DIMOSTRAZIONE_FORMALE.md).
    """
    print(f"{'k':>3}  {'repunit_k':>32}  {'max_rhs':>32}  {'ratio':>8}  {'proven':>7}")
    for k in range(1, k_max + 1):
        repunit = (10**k - 1) // 9
        max_rhs = (k - 1) + 2 * 9**k
        ratio = repunit / max_rhs
        proven = ratio > 1
        print(f"{k:>3}  {repunit:>32}  {max_rhs:>32}  {ratio:>8.4f}  {str(proven):>7}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--search", action="store_true", help="Run pruned search k=2..14")
    parser.add_argument("--bounds", action="store_true", help="Print bound table")
    parser.add_argument("--lemma", action="store_true", help="Print one-non-1-digit lemma table")
    parser.add_argument(
        "--k-max-search",
        type=int,
        default=14,
        metavar="K",
        help="Upper limit for pruned search (default: 14; warning: >14 is slow)",
    )
    args = parser.parse_args()

    run_all = not (args.search or args.bounds or args.lemma)

    if run_all or args.bounds:
        print("=== Bound table (log10 scale) ===")
        print_bound_table()
        print()

    if run_all or args.search:
        print(f"=== Pruned exhaustive search (k=2..{args.k_max_search}) ===")
        run_pruned_search(k_max=args.k_max_search)
        print()

    if run_all or args.lemma:
        print("=== One-non-1-digit lemma: ratio repunit_k / max_rhs ===")
        one_non1_lemma_table()
        print()


if __name__ == "__main__":
    main()
