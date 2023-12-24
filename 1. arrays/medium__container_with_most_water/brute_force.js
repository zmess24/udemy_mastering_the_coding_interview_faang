/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
	let max = 0;

	for (let i = 0; i < height.length; i++) {
		for (let j = i + 1; j < height.length; j++) {
			let length = Math.min(height[i], height[j]);
			let width = j - i;
			let area = length * width;
			max = Max.max(max, area);
		}
	}

	return max;
};

// Time: O(n^2)
// Space: O(1)
