var searchRange = function (nums, target) {
	let ans = [-1, -1];
	let start = 0;
	let end = nums.length - 1;
	// First occurrence
	while (start <= end) {
		let mid = Math.floor((start + end) / 2);
		if (target == nums[mid]) {
			ans[0] = mid;
			end = mid - 1;
		} else if (target < nums[mid]) {
			end = mid - 1;
		} else {
			start = mid + 1;
		}
	}
	// Last occurrence
	start = 0;
	end = nums.length - 1;
	while (start <= end) {
		let mid = Math.floor((start + end) / 2);
		if (target == nums[mid]) {
			ans[1] = mid;
			start = mid + 1;
		} else if (target < nums[mid]) {
			end = mid - 1;
		} else {
			start = mid + 1;
		}
	}
	return ans;
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