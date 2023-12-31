/**
|--------------------------------------------------
| Input: 'beabeefeab'
| Output: 'babab'
|--------------------------------------------------
*/

function checkAlternating(tempString) {
	let left = 0,
		right = 1;

	while (right < tempString.length) {
		if (tempString[left] === tempString[right]) return 0;
		left++;
		right++;
	}

	return tempString.length;
}

function replaceAll(char, string) {
	let re = new RegExp(char, "g");
	return string.replace(re, "");
}

function alternate(s) {
	let uniqueChars = Array.from(new Set(s));
	let max = 0;

	for (let i = 0; i < uniqueChars.length; i++) {
		let re1 = new RegExp(s[i], "g");
		let tempString = s.replace(re1, "");

		for (let j = i + 1; uniqueChars.length; j++) {
			let re2 = new RegExp(s[j], "g");
			tempString = s.replace(re2, "");
			let count = checkAlternating(tempString);
			max = Math.max(max, count);
		}
	}

	return max;
}
