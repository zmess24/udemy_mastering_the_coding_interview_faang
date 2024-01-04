/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
	let currentNode = head;
	let currentPosition = 1;
	let start = head;

	// Get value of nodes = left - 1
	while (currentPosition < left) {
		start = currentNode;
		currentNode = currentNode.next;
		currentPosition++;
	}

	let newList = null;
	let tail = currentNode;

	// Perform reversal between and left and right indicies
	while (left <= currentPosition && currentPosition <= right) {
		let next = currentNode.next;
		currentNode.next = newList;
		newList = currentNode;
		currentNode = next;
		currentPosition++;
	}

	start.next = newList;
	tail.next = currentNode;

	return m > 1 ? head : newList;
};
