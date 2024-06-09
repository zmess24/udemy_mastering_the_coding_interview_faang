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
 * @return {number[]}
 */
var rightSideView = function (root) {
	const result = [];
	dfs(root, 0, result);
	return result;
};

function dfs(node, currentLevel, result) {
	// If node is undefined
	if (!node) return;
	// If currentLevel is greater than or equal to result length
	if (currentLevel >= result.length) result.push(node.val);

	if (node.right) dfs(node.right, currentLevel + 1, result);
	if (node.left) dfs(node.left, currentLevel + 1, result);
}

// Time Complexity: O(N)
// Space Complexity: O(N)
