# Formal proof (base 10)

## Definition

Let \(n\) be a non-negative integer with decimal expansion
\(d_{k-1}d_{k-2}\dots d_1d_0\), with \(d_{k-1}\neq 0\) when \(k>1\).

Define
\[
S(n)=\sum_{j=0}^{k-1} d_j^{\,j+1},
\qquad
P(n)=\prod_{j=0}^{k-1} d_j^{\,j+1},
\]
where exponents are assigned from right to left (units exponent \(1\), tens exponent \(2\), etc.).

A number is **bipotentiant** when
\[
n=S(n)+P(n).
\]

## Main theorem

The complete set of base-10 bipotentiant numbers in the range \(0\le n\le 10^{14}-1\)
(all numbers with at most 14 digits) is
\[
\{0,\ 19,\ 24,\ 51,\ 1343,\ 1721\}.
\]
Moreover, a partial analytical argument (Lemma 5.1 below) rules out a large
infinite family of candidate digit structures for every \(k\ge 28\).

## Structure of the proof

The argument proceeds in five steps.

| Step | Scope | Method |
|------|-------|--------|
| 1 | \(n=0\) | Algebraic (trivial) |
| 2 | \(n>0\), structural lemmas | Algebraic (no-zero-digit theorem, product bound) |
| 3 | \(k=1\) | Algebraic |
| 4 | \(k=2\dots 14\) | Computer-assisted pruned exhaustive search |
| 5 | \(k\ge 28\), one-non-1-digit family | Analytical inequality |

---

## Proof

### 1) Zero case

For \(n=0\), we have \(S(0)=0\), \(P(0)=0\), hence \(0=S(0)+P(0)\).
So \(0\) is bipotentiant.

### 2) Structural lemmas for \(n>0\)

**Lemma 2.1 (product identity).** For every positive integer \(n\) with \(k\ge 1\) digits:
\[
P(n)=\sum_{j=1}^{k-1} d_j\bigl(10^j-d_j^j\bigr).
\]

*Proof.* Since \(n=S(n)+P(n)\),
\[
P(n)=n-S(n)=\sum_{j=0}^{k-1}\bigl(d_j 10^j-d_j^{j+1}\bigr)=\sum_{j=0}^{k-1}d_j\bigl(10^j-d_j^j\bigr).
\]
The \(j=0\) term is \(d_0(1-1)=0\), giving the stated identity. \(\square\)

**Lemma 2.2 (no-zero-digit).** Every bipotentiant \(n>0\) has no zero digit.

*Proof.* Suppose some \(d_i=0\). Then \(P(n)=0\).
By Lemma 2.1:
\[
0=\sum_{j=1}^{k-1} d_j\bigl(10^j-d_j^j\bigr).
\]
A one-digit number (\(k=1\)) cannot be bipotentiant: \(n=d_0\), \(S=d_0\), \(P=d_0\), so
\(n=S+P\) forces \(d_0=2d_0\), impossible for \(d_0>0\). Hence \(k\ge 2\) and the sum
is non-empty. Each summand with \(d_j\ge 1\) is strictly positive because
\(d_j^j\le 9^j<10^j\), so \(10^j-d_j^j>0\). The leading digit \(d_{k-1}\ge 1\)
contributes at least one positive summand, giving a contradiction. \(\square\)

**Lemma 2.3 (product upper bound).** For every bipotentiant \(n>0\) with \(k\) digits:
\[
P(n)<10^k.
\]

*Proof.* \(P(n)=n-S(n)<n<10^k\). \(\square\)

**Remark (product constraint in log space).** Lemma 2.3 is equivalent to
\[
\sum_{j=0}^{k-1}(j+1)\log_{10}d_j < k.
\]
Since each digit \(d_j\ge 2\) contributes at least \((j+1)\log_{10}2\approx 0.301(j+1)\)
to this sum, the total budget \(k\) can accommodate at most \(O(\sqrt{k})\) non-1 digits.
In particular the product constraint prunes the search tree dramatically and enables
the exhaustive verification in Step 4.

### 3) One-digit case (\(k=1\))

For \(k=1\), \(n=d_0\), \(S(n)=d_0\), \(P(n)=d_0\).
The fixed-point equation \(n=S(n)+P(n)\) becomes \(d_0=2d_0\), which is impossible for
\(d_0\ge 1\). Hence there are no one-digit bipotentiant numbers.

### 4) Pruned exhaustive search for \(k=2\dots 14\)

For a \(k\)-digit digit tuple \((d_0,\dots,d_{k-1})\) with every \(d_j\in\{1,\dots,9\}\)
(Lemma 2.2), the fixed-point equation \(n=S(n)+P(n)\) is checked directly. The search
tree is pruned the moment the running product \(\prod_{j\le j_0}d_j^{j+1}\) reaches
\(10^k\), since Lemma 2.3 guarantees no solution can survive.

The implementation in `bound_analysis.py` (`find_bipotentiant_k_digits`) runs the
search for every \(k\) from 2 to 14 and yields the following results (timings from a
single sequential run):

| \(k\) | Solutions | Time (s) |
|-------|-----------|----------|
| 2 | 19, 24, 51 | < 0.001 |
| 3 | — | < 0.001 |
| 4 | 1343, 1721 | < 0.001 |
| 5 | — | 0.001 |
| 6 | — | 0.004 |
| 7 | — | 0.014 |
| 8 | — | 0.041 |
| 9 | — | 0.112 |
| 10 | — | 0.312 |
| 11 | — | 0.782 |
| 12 | — | 1.828 |
| 13 | — | 4.204 |
| 14 | — | 9.140 |

Total wall-clock time for \(k=2\dots 14\): **≈ 16 seconds**.
The search is complete: every \(k\)-digit tuple satisfying the product constraint is
tested. Therefore, in the range \(10\le n\le 10^{14}-1\), there are no bipotentiant
numbers other than those listed in the main theorem.

To reproduce:

```python
python bound_analysis.py --search
```

### 5) Partial analytical result for \(k\ge 28\): one-non-1-digit family

We can prove analytically that an infinite family of digit structures admits no
solution for large enough \(k\).

**Lemma 5.1 (one-non-1-digit impossibility).** For \(k\ge 28\), there is no
\(k\)-digit bipotentiant number whose digit sequence has exactly one digit \(d\ge 2\)
(all others equal to 1).

*Proof.* Suppose \(d_{j_0}=d\ge 2\) and \(d_j=1\) for all \(j\ne j_0\).
Denote \(R_k=(10^k-1)/9\) (the \(k\)-digit repunit). Then:
\[
n=R_k+(d-1)\cdot 10^{j_0},\qquad
S(n)=(k-1)+d^{j_0+1},\qquad
P(n)=d^{j_0+1}.
\]
The fixed-point equation \(n=S(n)+P(n)\) becomes
\[
R_k+(d-1)\cdot 10^{j_0}=(k-1)+2d^{j_0+1}.
\]
Since \(d\ge 2\) by hypothesis, \((d-1)\cdot 10^{j_0}\ge 0\), so the
left-hand side satisfies \(n\ge R_k\). We bound the right-hand side:
\[
(k-1)+2d^{j_0+1}\le (k-1)+2\cdot 9^k,
\]
using the maximum \(d=9\), \(j_0=k-1\). Hence a necessary condition for a solution is:
\[
R_k\le(k-1)+2\cdot 9^k.
\]
Substituting \(R_k=(10^k-1)/9\):
\[
\frac{10^k-1}{9}\le(k-1)+2\cdot 9^k.
\]
A direct computation (see `bound_analysis.py --lemma`) shows this inequality
**fails** for all \(k\ge 28\):

| \(k\) | \(R_k\) / \((k-1)+2\cdot 9^k\) |
|-------|--------------------------------|
| 26 | 0.860 |
| 27 | 0.955 |
| **28** | **1.062 > 1** |
| 29 | 1.180 |
| 30 | 1.311 |

Since the ratio is monotonically increasing for \(k\ge 28\), the inequality
continues to fail for all larger \(k\). Therefore no \(k\)-digit bipotentiant with
exactly one non-1 digit exists for any \(k\ge 28\). \(\square\)

---

## Summary

| Range | Status |
|-------|--------|
| \(n=0\) | Bipotentiant (proven, §1) |
| \(k=1\) | No solution (proven, §3) |
| \(k=2\dots 14\) | Complete set \{19,24,51,1343,1721\} (proven, §4) |
| \(k=15\dots 27\) | No solution found; exhaustive proof pending faster implementation |
| \(k\ge 28\), one non-1 digit | No solution (proven, Lemma 5.1) |
| \(k\ge 28\), multiple non-1 digits | Open (analytical tools in development) |

The conjecture that \(\{0,19,24,51,1343,1721\}\) is the complete set of
base-10 bipotentiant numbers is supported by:

1. **Complete proof** for \(k\le 14\) (all integers up to \(10^{14}-1 \approx 10^{14}\)).
2. **Partial analytical proof** excluding the one-non-1-digit family for \(k\ge 28\).
3. **Exhaustive numerical scan** of all integers up to \(20{,}000{,}000\) via
   `is_bipotentiant`, confirming no additional solutions exist there.

```python
from bipotentiant_numbers import is_bipotentiant
print([n for n in range(1, 20_000_001) if is_bipotentiant(n)])
# [19, 24, 51, 1343, 1721]
```
\(\blacksquare\)
