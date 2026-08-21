# bipotentiant-numbers

Definition (Bipotentiant Numbers).

Let n be a positive integer with decimal representation

n = d_{k-1}d_{k-2}...d_1d_0,

where d_0 is the units digit and d_{k-1} ≠ 0. Define

S(n) = Σ_{j=0}^{k-1} d_j^{j+1}

and

P(n) = Π_{j=0}^{k-1} d_j^{j+1}.

We call n a bipotentiant number if

n = S(n) + P(n).

Equivalently,

n = Σ_{j=0}^{k-1} d_j^{j+1}
    + Π_{j=0}^{k-1} d_j^{j+1}.

The exponents are consecutive positive integers 1, 2, ..., k, assigned to the digits from right to left, starting with exponent 1 for the units digit.

For example, 19 is bipotentiant because

19 = (9^1 + 1^2) + (9^1 × 1^2)
   = 10 + 9
   = 19.

Definition (Bipotentiant Function).

Let n be a positive integer with decimal representation

n = d_{k-1}d_{k-2}...d_1d_0.

The bipotentiant function B is defined by

B(n) = Σ_{j=0}^{k-1} d_j^{j+1}
       + Π_{j=0}^{k-1} d_j^{j+1}.

Thus, B(n) is the integer obtained by applying the consecutive positive integer exponents 1, 2, ..., k to the decimal digits of n from right to left, and then adding the resulting sum and product.

In particular, n is a bipotentiant number if and only if

B(n) = n.

Definition (Bipotentiant Sequence).

The bipotentiant sequence is the sequence

(B(n))_{n≥1}

of positive integers obtained by applying the bipotentiant function B to the positive integers in their natural order. That is,

B(1), B(2), B(3), ..., B(n), ...

where each term is given by

B(n) = Σ_{j=0}^{k-1} d_j^{j+1}
       + Π_{j=0}^{k-1} d_j^{j+1},

with d_{k-1}d_{k-2}...d_1d_0 the decimal representation of n.

For example,

B(19) = 19,

so 19 occurs as the nineteenth term of the bipotentiant sequence.

In base 10, the first six bipotentiant numbers (including `0`) are:
`0, 19, 24, 51, 1343, 1721`.

## Usage

Run the module directly to list all bipotentiant numbers up to a limit:

```bash
python bipotentiant_numbers.py 1000
```
