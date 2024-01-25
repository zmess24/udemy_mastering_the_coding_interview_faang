A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are to from to as shown below:

image

The weight of a string is the sum of the weights of its characters. For example:

image

A uniform string consists of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not.
Given a string, , let be the set of weights for all possible uniform contiguous substrings of string . There will be queries to answer where each query consists of a single integer. Create a return array where for each query, the value is Yes if . Otherwise, append No.

Note: The symbol denotes that is an element of set .

Example

.

Working from left to right, weights that exist are:

string weight
a 1
b 2
bb 4
c 3
cc 6
ccc 9
d 4
dd 8
ddd 12
dddd 16
Now for each value in , see if it exists in the possible string weights. The return array is ['Yes', 'No', 'No', 'Yes', 'No'].
