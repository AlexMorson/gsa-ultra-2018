# Recreation through recreating

## Problem Statement

You are given two strings `A` and `B` consisting of lowercase characters from
the English alphabet. The maximum length of each string is `10^5`.

Your aim is to generate `A` by concatenating a minimum number of copies of `B`.
Before concatenating a copy of string `B` you can choose to remove any number of
characters from that copy.

It is guaranteed that it is possible to create string `A` using a finite number
of copies of string `B` in this way.

Write a function that takes two strings `A` and `B` as inputs, and outputs the
minimum number of copies of string `B` required to make string `A`.

For example, the output of `solution('xyxy', 'xyy')` would be `2`. We can
generate string `xyxy` by concatenating two modified copies of `xyy` as follows:

  - Create a first instance of `xyy`
  
  - Remove either the second or the third character, giving `xy`
  
  - Create a second instance of `xyy`
  
  - Again remove either the second or the third character, giving `xy`
  
  - Concatenate the two strings to give `xyxy`

## My Solution

My first solution was to loop through every character in B until I found the next character in A. This was too slow though.

So I did a bit of preprocessing, creating a dictionary with the keys being characters, and the values being a list of all the indices that the character appears at.
e.g., The string `"abb"` would get the dictionary `{"a": [0], "b": [1, 2]}`.
This meant that if a character only appears once in the whole string, it would not have to be searched all the way to find that one character, making it much faster.
