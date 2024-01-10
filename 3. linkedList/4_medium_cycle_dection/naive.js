/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
	let curretNode = head;
	const seenNodes = new Set();

	// Check if currentNode has been stored already
	while (!seenNodes.has(curretNode)) {
		// If currentNode has a taill, break and return false
		if (curretNode.next === null) {
			return false;
		}

		seenNodes.add(curretNode);
		curretNode = curretNode.next;
	}

	return true;
};

// Time Complexity: O(n)
// Space Complexity: O(N)
