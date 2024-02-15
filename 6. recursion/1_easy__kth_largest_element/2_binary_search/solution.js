```
Input:
k = 5
a = [1, 3, 3, 5, 5, 5, 8, 9]

Output:
[3, 5]
```;

/**
|--------------------------------------------------
| Zac
|--------------------------------------------------
*/

const searchRange = function (nums, target) {
	if (array.length === 0) return [-1, -1];
	// Find first position target element in array
	const firstPosition = binarySearch(nums, 0, nums.length - 1, target);
	if (firstPosition === -1) return [-1, -1];

	let startPos = firstPosition;
	let endPos = firstPosition;
	let temp1;
	let temp2;

	while (startPos !== -1) {
		temp1 = startPos;
		startPos = binarySearch(nums, 0, startPos - 1, target);
	}

	startPos = temp1;

	while (endPos !== -1) {
		temp2 = endPos;
		endPos = binarySearch(nums, endPos + 1, nums.length - 1, target);
	}

	endPos = temp2;

	return [startPos, endPos];
};

const binarySearch = function (array, left, right, target) {
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		const foundValue = array[mid];

		if (foundValue === target) {
			return mid;
		} else if (foundValue < target) {
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}

	return -1;
};
