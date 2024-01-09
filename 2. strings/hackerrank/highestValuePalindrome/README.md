# <a href="https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true">Highest Value Palindrome</a>

Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example is valid, is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.

### Examples

```
Input:

s = 1231
k = 3

Output:
9339

```

```
Input:

s = 12321
k = 1

Output:
12921

```

```
Input:

s = 12321
k = 1

Output:
12921

```

Input:

s = 3943
k = 1

Output:
3993

```

```

Input:

s = 092282
k = 3

Output:
992299

```

```
