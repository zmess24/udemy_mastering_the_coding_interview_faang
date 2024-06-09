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
 * @return {boolean}
 */
var isValidBST = function (root) {
	if (!root) return true;
	return dfs(root, -Infinity, Infinity);
};

function dfs(node, min, max) {
	if (node.val <= min || node.val >= max) {
		return false;
	}

	if (node.left) {
		let leftIsValid = dfs(node.left, min, node.val);
		if (!leftIsValid) return false;
	}

	if (node.right) {
		let rightIsValid = dfs(node.right, node.val, max);
		if (!rightIsValid) return false;
	}

	return true;
}
