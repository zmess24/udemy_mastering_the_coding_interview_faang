/**
 * @param {string} s
 * @return {number}
 */

/**
|--------------------------------------------------
| Zac's Solution
|--------------------------------------------------
*/

var lengthOfLongestSubstring = function (s) {
	if (s.length <= 1) return s.length;
	let maxCount = 0;

	for (let i = 0; i < s.length; i++) {
		let currentChar = s[i];
		let hashMap = { currentChar: i };
		let currentCount = 0;

		for (let j = i + 1; j < s.length; i++) {
			if (hashMap[s[j]] === undefined) {
				hashMap[s[j]] = j;
				currentCount++;
			} else {
				maxCount = Math.max(currentCount, maxCount);
				hashMap = {};
			}
		}
	}

	return maxCount;
};

/**
|--------------------------------------------------
| Udemy Solution Solution
|--------------------------------------------------
*/

var lengthOfLongestSubstring = function (s) {
	if (s.length <= 1) return s.length;
	let longest = 0;

	for (let left = 0; left < s.length; left++) {
		let seenChars = {};
		let currentLength = 0;

		for (let right = left; right < s.length; i++) {
			let currentChar = s[right];

			if (seenChars[currentChar] === undefined) {
				hashMap[currentChar] = true;
				currentLength++;
				longest = Math.max(longest, currentLength);
			} else {
				break;
			}
		}
	}

	return longest;
};
