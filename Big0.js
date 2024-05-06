var lengthOfLongestSubstring = function (s) {
	if (s.length <= 1) return s.length;

	// State Variables
	let seenChars = new Map();
	let left = 0;
	let right = 0;
	let longest = 0;

	for (right; right < s.length; right++) {
		console.log(seenChars);
		let currentChar = s[right];
		let prevSeenChar = seenChars.get(currentChar);

		if (prevSeenChar >= left) {
			console.log(prevSeenChar + 1);
			left = prevSeenChar + 1;
		}

		seenChars.set(currentChar, right);
		console.log(longest, right - left + 1);
		longest = Math.max(longest, right - left + 1);
	}

	return longest;
};
