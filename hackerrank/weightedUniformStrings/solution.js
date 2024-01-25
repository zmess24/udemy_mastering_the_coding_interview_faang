function getWeight(letter, left, right) {
	let alphabet = "abcdefghijklmnopqrstuvwxyz";
	let weight = right - left + 1;
	return (alphabet.indexOf(letter) + 1) * weight;
}

function weightedUniformStrings(s, queries) {
	let left = 0;
	let right = 0;
	let hashMap = new Map();

	while (right < s.length) {
		if (s[right] !== s[left]) {
			left = right;
		}

		let currentWeight = getWeight(s[left], left, right);
		hashMap.set(currentWeight, s[left]);
		right++;
	}

	return queries.map((q) => {
		return hashMap.get(q) ? "Yes" : "No";
	});
}
