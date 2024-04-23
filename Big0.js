/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function (nums, k) {
	let n = nums.length;

	// Init Window
	window = [];

	for (let i = 0; i < k; i++) {
		window.push(nums[i]);
	}

	for (let i = k; i < n; i++) {
		let current_min = Math.min(window);
		print(current_min);
	}
};
