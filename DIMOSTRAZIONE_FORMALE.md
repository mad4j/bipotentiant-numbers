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

## Theorem (fully proven scope)

In the interval \(0 \le n \le 999999\), the complete set of base-10 bipotentiant numbers is:
\[
\{0,\ 19,\ 24,\ 51,\ 1343,\ 1721\}.
\]

In particular, there are no 5-digit or 6-digit bipotentiant numbers.

## Conjectural global statement

The same set is currently the only known set globally (without digit-count restriction):
\[
\{0,\ 19,\ 24,\ 51,\ 1343,\ 1721\}.
\]
This document proves the statement on the fully verified range above and reports larger exhaustive scans as supporting evidence.

## Proof

### 1) Zero case

For \(n=0\), we have \(S(0)=0\), \(P(0)=0\), hence \(0=S(0)+P(0)\).
So \(0\) is bipotentiant.

### 2) Structural identity for \(n>0\)

For \(n>0\), write
\[
n=\sum_{j=0}^{k-1} d_j\,10^j.
\]
Since \(n=S(n)+P(n)\),
\[
P(n)=n-S(n)=\sum_{j=0}^{k-1}\bigl(d_j10^j-d_j^{j+1}\bigr).
\]
So
\[
P(n)=\sum_{j=1}^{k-1} d_j\bigl(10^j-d_j^j\bigr),
\]
because the \(j=0\) term is \(d_0-d_0=0\).

If any digit \(d_t=0\), then \(P(n)=0\).  
But the last formula is a sum of non-negative terms, and for any \(j\ge 1\), \(d_j\in\{1,\dots,9\}\) implies
\[
d_j\bigl(10^j-d_j^j\bigr)>0.
\]
Hence for \(n>0\), all digits must be non-zero.

### 3) Exhaustive verification (computer-assisted, same formal definition)

Using the project implementation of `is_bipotentiant` (which is exactly the definition above), exhaustive evaluation returns:

- up to \(999999\): \(19,24,51,1343,1721\);
- up to \(20{,}000{,}000\): still \(19,24,51,1343,1721\) (no additional hits).

Therefore, in the checked domain, there are no 5-digit or 6-digit bipotentiant numbers.

### 4) Proven conclusion

Combining:
1. the exact algebraic characterization above,
2. and exhaustive verification under that exact definition on \(0\le n\le 999999\),

the only base-10 bipotentiant numbers in the proven interval are
\[
\{0,\ 19,\ 24,\ 51,\ 1343,\ 1721\}.
\]
Additionally, exhaustive scanning up to \(20{,}000{,}000\) yields no further examples.
\(\blacksquare\)
