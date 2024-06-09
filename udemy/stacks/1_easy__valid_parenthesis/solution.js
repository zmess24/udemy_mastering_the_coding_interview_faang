/**
|--------------------------------------------------
| Zac's Solution #1
|--------------------------------------------------
*/

/**
 * @param {string} s
 * @return {boolean}
 */

var isValid = function (s) {
	if (s === "") return true;
	if (s.length % 2 === 1) return false;

	const stack = [];
	const map = { "{": "}", "[": "]", "(": ")" };

	for (let i = 0; i < s.length; i++) {
		let currentChar = s[i];

		// Check if character is left or right bracket.
		if ("[({".indexOf(currentChar) > -1) {
			stack.push(currentChar);
		} else {
			let lastChar = stack.pop();
			if (map[lastChar] !== currentChar) return false;
		}
	}

	return stack.length === 0 ? true : false;
};

/**
|--------------------------------------------------
| Udemy Solution
|--------------------------------------------------
*/

var isValid = function (s) {
	if (s === "") return true;

	const stack = [];
	const map = { "{": "}", "[": "]", "(": ")" };

	for (let i = 0; i < s.length; i++) {
		// Check if character is left or right bracket.
		if (map[s[i]]) {
			stack.push(s[i]);
		} else {
			let leftChar = stack.pop();
			let correctBracker = map[leftChar];
			if (s[i] !== correctBracker) return false;
		}
	}

	return stack.length === 0;
};

// Space Complexity: O(n)
// Time Complexity: O(n)
