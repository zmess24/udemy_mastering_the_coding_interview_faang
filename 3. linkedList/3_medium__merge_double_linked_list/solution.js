/**
 * // Definition for a Node.
 * function Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var flatten = function (head) {
	// If head === null
	if (!head) return head;
	let currentNode = head;
	// Iterate through LinkedList
	while (currentNode !== null) {
		if (currentNode.child === null) {
			// If currentNode doesn't have child, move forward.
			currentNode = currentNode.next;
		} else {
			let tail = currentNode.child;
			// Iterate through child linkedList until reach last node
			while (tail.next !== null) {
				tail = tail.next;
			}
			// Set tails next value to currentNode's next value.
			tail.next = currentNode.next;

			// Point the next nodes previous value to the current tail.
			if (tail.next !== null) {
				tail.next.prev = tail;
			}

			// Set currentNode's next value = child node
			currentNode.next = currentNode.child;
			// Set CurrentNode's next previousChild  = current Node
			currentNode.next.prev = currentNode;
			// Eliminate Child Node
			currentNode.child = null;
		}
	}

	return head;
};

// Space Compleity: O(1)
// Time Complexity: O(N)
