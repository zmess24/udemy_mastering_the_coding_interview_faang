/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
	let totalWater = 0;
	let left = 0;
	let right = height.length - 1;
	let maxLeft = 0;
	let maxRight = 0;

	while (left < right) {
		console.log({ left: height[left], right: height[right], maxLeft, maxRight });
		if (height[left] <= height[right]) {
			if (height[left] >= maxLeft) {
				maxLeft = height[left];
			} else {
				console.log("ADD LEFT", { difference: maxLeft - height[left] });
				totalWater += maxLeft - height[left];
			}
			left++;
		} else {
			if (height[right] >= maxRight) {
				maxRight = height[right];
			} else {
				console.log("ADD RIGHT", { difference: maxRight - height[right] });
				totalWater += maxRight - height[right];
			}
			right--;
		}
	}

	return totalWater;
};

// Time: O(N)
// Space O(1)
