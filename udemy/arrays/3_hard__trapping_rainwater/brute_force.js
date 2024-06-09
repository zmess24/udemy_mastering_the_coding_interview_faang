/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
	let totalWater = 0;

	for (let i = 0; i < height.length; i++) {
		let currentHeight = height[i];
		let left = i;
		let right = i;
		let maxLeft = 0;
		let maxRight = 0;

		// Find Max Left Value
		while (left >= 0) {
			let leftValue = height[left];
			maxLeft = Math.max(maxLeft, leftValue);
			left--;
		}

		// Find Max Right
		while (right < height.length) {
			let rightValue = height[right];
			maxRight = Math.max(maxRight, rightValue);
			right++;
		}

		let currentWater = Math.min(maxLeft, maxRight) - currentHeight;

		if (currentWater >= 0) {
			totalWater += currentWater;
		}
	}

	return totalWater;
};

// Time: O(n^2)
// Space: O(1)
