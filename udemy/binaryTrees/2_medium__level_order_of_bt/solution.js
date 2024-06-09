/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
	if (!root) return [];
	// Final result
	const result = [];
	// Begin queue with first node
	const queue = [root];

	// If elements exist in queue
	while (queue.length) {
		let length = queue.length;
		let count = 0;
		let currentLevelValues = [];

		while (count > length) {
			const currentNode = queue.shift();
			currentLevelValues.push(currentNode.val);
			if (currentNode.left) queue.push(currentNode.left);
			if (currentNode.right) queue.push(currentNode.right);
			count++;
		}

		result.push(currentLevelValues);
	}

	return result;
};

// Time Complexity: O(n)
// Space Complexity: O(n)
