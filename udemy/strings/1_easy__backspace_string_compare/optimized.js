/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

/**
|--------------------------------------------------
| Zac's Solution
|--------------------------------------------------
*/

var backspaceCompare = function (s, t) {
	let longer, shorter;
	let longerA = [],
		shorterA = [];

	if (s.length >= t.length) {
		longer = s;
		shorter = t;
	} else {
		longer = t;
		shorter = s;
	}

	for (let i = 0; i < longer.length; i++) {
		longer[i] === "#" ? longerA.pop() : longerA.push(longer[i]);
		if (shorter[i] !== undefined) shorter[i] === "#" ? shorterA.pop() : shorterA.push(shorter[i]);
	}

	longerA = longerA.join("");
	shorterA = shorterA.join("");

	return longerA === shorterA ? true : false;
};

/**
|--------------------------------------------------
| Udemy Solution
|--------------------------------------------------
*/

var backspaceCompare = function (s, t) {
	let ps = s.length - 1,
		pt = t.length - 1;

	while (ps >= 0 || pt >= 0) {
		if (s[ps] === "#" || t[pt] === "#") {
			if (s[ps] === "#") {
				let backCount = 2;

				while (backCount > 0) {
					ps--;
					backCount--;
					if (s[ps] === "#") {
						backCount = backCount + 2;
					}
				}
			}

			if (t[pt] === "#") {
				let backCount = 2;

				while (backCount > 0) {
					pt--;
					backCount--;
					if (t[pt] === "#") {
						backCount = backCount + 2;
					}
				}
			}
		} else {
			if (s[ps] !== t[pt]) {
				return false;
			} else {
				ps--;
				pt--;
			}
		}
	}

	return true;
};

/**
|--------------------------------------------------
| LeetCode Clean Solution
|--------------------------------------------------
*/

function backspaceCompare(s, t) {
	let n = s.length;
	let m = t.length;

	let hashCounter1 = 0;
	let hashCounter2 = 0;

	while (n >= 0 || m >= 0) {
		while (n >= 0) {
			// if the character is `#`
			// then increase the hashcounter value
			if (s[n] === "#") {
				hashCounter1++;
			}
			// else if the hash counter's value is gt 0
			// then skip the characters till the value becomes 0
			else if (hashCounter1 > 0) {
				hashCounter1--;
			}
			// else we need to now compare the non-hash characters
			// so break out of the loop
			else {
				break;
			}
			// keep decrementing else we'll be in infinite loop
			n--;
		}

		while (m >= 0) {
			if (t[m] === "#") {
				hashCounter2++;
			} else if (hashCounter2 > 0) {
				hashCounter2--;
			} else {
				break;
			}
			m--;
		}

		// now check if the characters are equal
		// if they're not equal then return false
		const char1 = n < 0 ? "" : s[n];
		const char2 = m < 0 ? "" : t[m];

		if (char1 !== char2) return false;

		n--;
		m--;
	}

	return true;
}
