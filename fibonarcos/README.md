# Fibonarcos

## Problem Statement

Jimmy's dangerous "just one more episode" mentality when binge-watching his
favourite TV shows has led him to investigate the Fibonacci sequence, a series
of numbers in which each number (Fibonacci number) is the sum of the two
preceding numbers and first two numbers are `1` i.e. the series 
`1, 1, 2, 3, 5, 8, ...`

Now, he's curious which natural numbers can be expressed as the product of
powers of Fibonacci numbers only. For example, 5 (which is just the Fibonacci
number 5), 9 (which is `3^2`), and 12 (which is `2^2 x 3`) can all be expressed
as the product of powers of Fibonacci numbers whereas 11 can't be.  Formally,
whether a number is expressible as `f_1^{p1} × f_2^{p2} × ...` where `f_i` is a
Fibonacci number and `p_i > 0`, for all i.

Write a function that takes two positive integers L and R
(1 ≤ L ≤ R ≤ 10^{18}, 1 ≤ R - L + 1 ≤ 10^6) as inputs, and outputs the number of
integers in this range (both L and R inclusive) which cannot be expressed as the
product of powers of Fibonacci numbers.

For example, the output of `solution(3, 9)` is `1`, as `7` is the only integer
in the range which cannot be expressed as the product of powers of Fibonacci
numbers.

## My Solution

I constructed a list of "useful" fibonacci numbers. Meaning they couldn't be made from a product of fibonacci numbers before it.
Then, starting with the largest of these numbers, I looped through them, divding them out of the number if possible.
If I am left with 1, then clearly the number could be written as a product of fibonacci numbers, otherwise it couldn't.

I'm not sure if this method is guaranteed to work though... I'd be interested to see a proof.
