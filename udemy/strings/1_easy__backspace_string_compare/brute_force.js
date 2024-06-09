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
	let newS = [];
	let newT = [];

	for (let i = 0; i < s.length; i++) {
		if (s[i] === "#") {
			newS.pop();
		} else {
			newS.push(s[i]);
		}
	}

	for (let i = 0; i < t.length; i++) {
		if (t[i] === "#") {
			newT.pop();
		} else {
			newT.push(t[i]);
		}
	}

	newS = newS.join("");
	newT = newT.join("");

	return newS === newT ? true : false;
};

/**
|--------------------------------------------------
| Udemy Solution Solution
|--------------------------------------------------
*/
