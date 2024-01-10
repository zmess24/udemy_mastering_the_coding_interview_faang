/**
|--------------------------------------------------
| Floyd's Tortoise & Hair Algorithm
|--------------------------------------------------
*/

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
	let hare = head;
	let tortoise = head;

	// Check if currentNode has been stored already
	while (true) {
		hare = hare.next;
		tortoise = tortoise.next;

		if (hare === null || hare.next === null) {
			return false;
		} else {
			hare = hare.next;
		}

		if (tortoise === hare) break;
	}

	let p1 = head;
	let p2 = tortoise;

	while (p1 !== p2) {
		p1 = p1.next;
		p2 = p2.next;
	}

	return p1;
};

// Time Complexity: O(n)
// Space Complexity: O(1)
