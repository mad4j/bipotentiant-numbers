# bipotentiant-numbers

Utilities for working with bipotentiant numbers.

## Definition

Let `n` be a positive integer with decimal representation `d_{k-1}...d_1d_0`,
where `d_0` is the units digit. Define:

- `S(n) = Σ d_j^(j+1)`
- `P(n) = Π d_j^(j+1)`

with exponents assigned from right to left, starting at `1` for the units
digit.

`n` is **bipotentiant** when:

`n = S(n) + P(n)`

For example, `19` is bipotentiant because:

`19 = (9^1 + 1^2) + (9^1 × 1^2) = 10 + 9`

In base 10, the first six bipotentiant numbers (including `0`) are:
`0, 19, 24, 51, 1343, 1721`.

## Usage

Run the module directly to list all bipotentiant numbers up to a limit:

```bash
python bipotentiant_numbers.py 1000
```
