/**
 * @param {string} s
 * @return {number}
 */

/**
|--------------------------------------------------
| Zac's Solution #1
|--------------------------------------------------
*/

var lengthOfLongestSubstring = function (s) {
	if (s.length === 0) return 0;
	if (s.length === 1) return 1;
	// Set Max Count and currentCount
	let maxCount = 0,
		currentCount = 1;

	// Initialize Hashmap with first value
	let hashMap = { [s[0]]: 0 };

	// Intitialize two pointers
	let left = 0,
		right = 1;

	while (right < s.length) {
		let rightChar = s[right];

		if (hashMap[rightChar] === undefined) {
			hashMap[rightChar] = right;
			currentCount++;
			right++;
		} else {
			maxCount = Math.max(currentCount, maxCount);
			delete hashMap[s[left]];
			currentCount--;
			left++;
		}
	}

	maxCount = Math.max(currentCount, maxCount);

	return maxCount;
};

/**
|--------------------------------------------------
| Udemy Solution
|--------------------------------------------------
*/

var lengthOfLongestSubstring = function (s) {
	if (s.length <= 1) return s.length;

	// State Variables
	// let seenChars = {};
	let seenChars = new Map();
	let left = 0;
	let right = 0;
	let longest = 0;

	for (right; right < s.length; right++) {
		let currentChar = s[right];
		let prevSeenChar = seenChars.get(currentChar);

		if (prevSeenChar >= left) {
			left = prevSeenChar + 1;
		}

		seenChars.set(currentChar, right);
		longest = Math.max(longest, right - left + 1);
	}

	return longest;
};

/**
|--------------------------------------------------
| Alternative LeetCode Solution
|--------------------------------------------------
*/

var lengthOfLongestSubstring = function (s) {
	let set = new Set();
	let left = 0;
	let maxSize = 0;

	if (s.length === 0) return 0;
	if (s.length === 1) return 1;

	for (let i = 0; i < s.length; i++) {
		while (set.has(s[i])) {
			set.delete(s[left]);
			left++;
		}
		set.add(s[i]);
		maxSize = Math.max(maxSize, i - left + 1);
	}
	return maxSize;
};
