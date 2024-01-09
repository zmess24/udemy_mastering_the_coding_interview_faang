# Linked List

A linked list is a chain of a data structure known as a `ListNode`.

A `ListNode` has two properties on it:

-   `value`: Any value can be assigned to it (string, number, ect)
-   `next`: Points to another ListNode or null

```js
class ListNode {
	value: any;
	next: ListNode;
}
```

A `head` list node is the very first listNode, and the `tail` is the very last ListNode. Not all linkedLists have a tail
