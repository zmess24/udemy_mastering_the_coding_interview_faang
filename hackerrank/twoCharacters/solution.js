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
		let tempString = replaceAll(s[i], s);

		for (let j = i + 1; uniqueChars.length; j++) {
			tempString = replaceAll(s[j], s);
			let count = checkAlternating(tempString);
			max = Math.max(max, count);
		}
	}

	return max;
}
