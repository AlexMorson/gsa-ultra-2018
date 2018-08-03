# Fearful symmetry

## Problem Statement

A string is a palindrome if it reads the same backwards as forwards. For
instance, `cabac` and `beeb` are palindromes, but `abb` is not.

Given a string T, we define the "score" of T as the length of the longest
palindrome that can be constructed by using some of the characters of T. For
instance, the score of `T = 'abc'` is 1, corresponding to the possible
palindromes `a`, `b` or `c`. The score of `T = 'aacggg'` is 5, corresponding to
the palindrome `gacag`.

Write a function that takes as input a string S consisting of N characters
(`200 ≤ N ≤ 5000`), each from the set `{'a', 'b', 'c', 'd', 'e', 'f', 'g'}`.
Your function should split S into four non-overlapping pieces such that:

  - Each piece has non-zero length
  - Each piece consists of contiguous characters
  - The sum of the scores of each piece is minimised

Your function should return the minimum total score for S.

For instance, if `S = 'abccaa'` then the total minimum score is 4. Splitting S
into the four pieces 'abc', 'c', 'a', 'a' gives the total score
1 + 1 + 1 + 1 = 4. It is easy to see that it is not possible to obtain a lower
score. Observe that if the string was instead split as 'a', 'b', 'cc', 'aa' then
the total score would be 1 + 1 + 2 + 2 = 6.

## My Solution

I spent a long, long time trying to figure out if I could solve this problem by splitting it into 2 parts optimally, and then splitting each of those parts optimally. I finally stumbled upon a counterexample for which this did not work: `"abccbaabccba"` (as the optimal way of splitting into two parts is `abc cbaabccba`, but the optimal solution would be `abc cba abc cba`).

So I started with a brute force solution, obviously too slow. Next I tried precomputing the score for every subsequence (in a similar way to Flower Power). Better, but still too slow for the largest inputs that the problem could give.

Then I realised that in my inner loop (moving the third split along) the score can only ever change by 1 each iteration, so I can move the split further if the current score is much larger than the best score so far. This skipped almost all the work, but was still slightly too slow for the largest inputs.

Finally I noticed that I could replace the whole inner loop by a lookup if I precalculated the optimal way to split a subsequence s[i:] into two parts. This meant that my whole solution is now O(n^2) rather than O(n^3), hooray, it is now fast enough!
