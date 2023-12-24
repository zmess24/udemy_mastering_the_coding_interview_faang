function twoSum(arr, t) {
	let hashMap = {};

	for (let i = 0; i < arr.length; i++) {
		let currentMapValue = hashMap[arr[i]];
		if (currentMapValue >= 0) {
			return [currentMapValue, i];
		} else {
			let numberToFind = t - arr[i];
			hashMap[numberToFind] = i;
		}
	}

	return null;
}
