function highestValuePalindrome(s, n, k) {
	let left = 0,
		right = s.length - 1;

	while (k !== 0) {
		if (s[left] !== s[right]) {
			if (parseInt(s[left]) < parseInt(s[right])) {
				s = s.split("").replace(left, 1, s[right]).join("");
			} else {
				s = s.split("").replace(left, 1, s[right]).join("");
			}
			k = k - 1;
		}

		if (left > right) {
			left = 0;
			right = s.length - 1;
		}
	}

	return s;
}
