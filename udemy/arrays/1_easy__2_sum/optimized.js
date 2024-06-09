/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(arr, t) {
	let hashMap = {};

	for (let i = 0; i < arr.length; i++) {
		let currentMapValue = hashMap[arr[i]];
		if (currentMapValue !== undefined) {
			return [currentMapValue, i];
		} else {
			let numberToFind = t - arr[i];
			hashMap[numberToFind] = i;
		}
	}

	return null;
}

// Time Complexity: O(N) e.g quadratic relationship
// Space Complexity: O(N)
