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
 * @return {number}
 */
var countNodes = function (root) {
	if (!root) return 0;
	const height = getTreeHeight(root);
	if (height === 0) return 1;
	const upperCount = Math.pow(2, height) - 1;
	let left = 0;
	let right = upperCount;

	while (left < right) {
		let indexToFind = Math.ceil((left + right) / 2);
		let exists = nodeExists(indexToFind, height, root);
		if (exists) {
			left = indexToFind;
		} else {
			right = indexToFind - 1;
		}
	}

	return upperCount + left + 1;
};

function getTreeHeight(root) {
	let height = 0;
	while (root.left !== null) {
		height++;
		root = root.left;
	}
	return height;
}

function nodeExists(indexToFind, height, node) {
	let left = 0;
	let right = Math.pow(2, height);
	let count = 0;

	while (count < height) {
		let midOfNode = Math.ceil((left + right) / 2);
		if (indexToFind >= midOfNode) {
			node = node.right;
			left = midOfNode;
		} else {
			node = node.left;
			right = midOfNode;
		}

		count++;
	}

	return node !== null;
}
