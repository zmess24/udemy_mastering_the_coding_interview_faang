function twoSum(arr, t) {
	let answer = null;

	for (let i = 0; i < arr.length; i++) {
		let currentNumber = arr[i];

		for (let j = i + 1; j < arr.length; j++) {
			let nextNumber = arr[j];

			if (currentNumber + nextNumber === t) {
				answer = [i, j];
				break;
			}
		}

		if (answer !== null) {
			break;
		}
	}

	return answer;
}

// Time Complexity: O(n*n) e.g quadratic relationship
// Space Complexity: 0(1)
