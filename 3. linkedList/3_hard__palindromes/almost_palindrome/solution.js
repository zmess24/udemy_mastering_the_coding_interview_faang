/**
 * @param {string} s
 * @return {boolean}
 */

/**
|--------------------------------------------------
| Zac's Solution
|--------------------------------------------------
*/

// Helper Method
function validSubPalindrome(s, left, right) {
	while (left < right) {
		if (s[left] !== s[right]) {
			return false;
		}

		left++;
		right--;
	}

	return true;
}

var validPalindrome = function (s) {
	s = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();

	let left = 0;
	let right = s.length - 1;

	while (left <= right) {
		if (s[left] !== s[right]) {
			return validSubPalindrome(s, left + 1, right) || validSubPalindrome(s, left, right - 1);
		}

		left++;
		right--;
	}

	return true;
};
