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

The complete set of base-10 bipotentiant numbers in the range \(0\le n\le 10^{18}-1\)
(all numbers with at most 18 digits) is
\[
\{0,\ 19,\ 24,\ 51,\ 1343,\ 1721\}.
\]
Moreover, a partial analytical argument (Lemma 5.1 below) rules out a large
infinite family of candidate digit structures for every \(k\ge 28\); two further
lemmas (5.2 and 5.3) sharpen the structure of surviving candidates.

## Structure of the proof

The argument proceeds in five steps.

| Step | Scope | Method |
|------|-------|--------|
| 1 | \(n=0\) | Algebraic (trivial) |
| 2 | \(n>0\), structural lemmas | Algebraic (no-zero-digit theorem, product bound) |
| 3 | \(k=1\) | Algebraic |
| 4 | \(k=2\dots 18\) | Computer-assisted pruned exhaustive search |
| 5 | \(k\ge 6\), all digits \(\ge 2\) | Analytical inequality (Lemma 5.2) |
| 6 | Any \(k\), \(m\) non-1 digits | Combinatorial upper bound on \(m\) (Lemma 5.3) |
| 7 | \(k\ge 28\), one-non-1-digit family | Analytical inequality (Lemma 5.1) |

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

### 4) Pruned exhaustive search for \(k=2\dots 18\)

For a \(k\)-digit digit tuple \((d_0,\dots,d_{k-1})\) with every \(d_j\in\{1,\dots,9\}\)
(Lemma 2.2), the fixed-point equation \(n=S(n)+P(n)\) is checked directly. The search
tree is pruned the moment the running product \(\prod_{j\le j_0}d_j^{j+1}\) reaches
\(10^k\), since Lemma 2.3 guarantees no solution can survive.

The implementation in `bound_analysis.py` (`find_bipotentiant_k_digits`) runs the
search for every \(k\) from 2 to 18 and yields the following results (timings from a
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
| 15 | — | 15.579 |
| 16 | — | 32.081 |
| 17 | — | 64.155 |
| 18 | — | 126.548 |

Total wall-clock time for \(k=2\dots 18\): **≈ 254 seconds**.
The search is complete: every \(k\)-digit tuple satisfying the product constraint is
tested. Therefore, in the range \(10\le n\le 10^{18}-1\), there are no bipotentiant
numbers other than those listed in the main theorem.

To reproduce:

```python
python bound_analysis.py --search
```

### 5) All-digits-non-1 impossibility for \(k\ge 6\) (Lemma 5.2)

**Lemma 5.2 (all-non-1-digit impossibility).** For \(k\ge 6\), no \(k\)-digit number
whose digit sequence consists entirely of digits \(\ge 2\) can be bipotentiant.

*Proof.* Suppose every \(d_j\ge 2\). Then
\[
P(n)=\prod_{j=0}^{k-1}d_j^{j+1}\ge\prod_{j=0}^{k-1}2^{j+1}=2^{\sum_{j=0}^{k-1}(j+1)}=2^{k(k+1)/2}.
\]
By Lemma 2.3, \(P(n)<10^k\), so \(2^{k(k+1)/2}<10^k\), i.e.
\(\tfrac{k+1}{2}\log_{10}2<1\), i.e. \(k<2/\log_{10}2-1=2\log_2 10-1\approx 5.64\).
Hence for \(k\ge 6\) the product constraint is violated, and no solution exists. \(\square\)

| \(k\) | \(k(k+1)/2\) | \(\log_{10}(\min P)\) | \(\log_{10}(10^k)\) | Impossible? |
|-------|-------------|----------------------|---------------------|-------------|
| 4 | 10 | 3.010 | 4 | No |
| 5 | 15 | 4.515 | 5 | No |
| **6** | **21** | **6.321** | **6** | **Yes** |
| 7 | 28 | 8.428 | 7 | Yes |
| 8 | 36 | 10.836 | 8 | Yes |

To verify:

```python
python bound_analysis.py --lemma52
```

### 6) Bound on the number of non-1 digits (Lemma 5.3)

**Lemma 5.3 (non-1-digit count bound).** In any \(k\)-digit bipotentiant number the
number of digits **not** equal to \(1\) is at most
\[
m_{\max}(k)=\left\lfloor\frac{-1+\sqrt{1+8k/\log_{10}2}}{2}\right\rfloor.
\]
In particular \(m_{\max}(k)=O\!\left(\sqrt{k}\right)\).

*Proof.* Let \(m\) be the number of non-1 digits, located at positions
\(j_1<j_2<\cdots<j_m\). The minimum product contribution is achieved when every
non-1 digit equals 2 and is placed at the lowest available positions
\(0,1,\ldots,m-1\):
\[
P(n)\ge\prod_{i=0}^{m-1}2^{i+1}=2^{m(m+1)/2}.
\]
The product constraint \(P(n)<10^k\) then forces
\(\tfrac{m(m+1)}{2}\log_{10}2<k\), giving the stated bound on \(m\). \(\square\)

| \(k\) | \(m_{\max}(k)\) |
|-------|--------------|
| 10 | 7 |
| 15 | 9 |
| 18 | 10 |
| 20 | 11 |
| 28 | 13 |
| 30 | 13 |

To verify:

```python
python bound_analysis.py --lemma53
```

### 7) Partial analytical result for \(k\ge 28\): one-non-1-digit family

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
| \(k=2\dots 18\) | Complete set \{19,24,51,1343,1721\} (proven, §4) |
| \(k\ge 6\), all digits \(\ge 2\) | No solution (proven, Lemma 5.2) |
| Any \(k\), \(m\) non-1 digits | \(m\le m_{\max}(k)=O(\sqrt{k})\) (proven, Lemma 5.3) |
| \(k=19\dots 27\) | No solution found; exhaustive proof pending faster implementation |
| \(k\ge 28\), one non-1 digit | No solution (proven, Lemma 5.1) |
| \(k\ge 28\), multiple non-1 digits | Open (analytical tools in development) |

The conjecture that \(\{0,19,24,51,1343,1721\}\) is the complete set of
base-10 bipotentiant numbers is supported by:

1. **Complete proof** for \(k\le 18\) (all integers up to \(10^{18}-1\approx 10^{18}\)).
2. **Partial analytical proof** excluding:
   - All-non-1-digit numbers for \(k\ge 6\) (Lemma 5.2).
   - The one-non-1-digit family for \(k\ge 28\) (Lemma 5.1).
3. **Structural bound** limiting any \(k\)-digit candidate to at most \(O(\sqrt{k})\)
   non-1 digits (Lemma 5.3).
4. **Exhaustive numerical scan** of all integers up to \(20{,}000{,}000\) via
   `is_bipotentiant`, confirming no additional solutions exist there.

```python
from bipotentiant_numbers import is_bipotentiant
print([n for n in range(1, 20_000_001) if is_bipotentiant(n)])
# [19, 24, 51, 1343, 1721]
```
\(\blacksquare\)
