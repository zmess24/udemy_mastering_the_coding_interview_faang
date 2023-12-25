// Shifting Window technique

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
	let max = 0;
	let left = 0;
	let right = height.length - 1;

	while (left !== right) {
		let length = Math.min(height[left], height[right]);
		let width = right - left;
		let area = length * width;
		max = Math.max(max, area);

		height[right] > height[left] ? left++ : right--;
	}

	return max;
};

// Time: O(n^2)
// Space: O(1)
