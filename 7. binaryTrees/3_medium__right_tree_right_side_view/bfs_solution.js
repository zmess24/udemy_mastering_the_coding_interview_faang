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
    if (!root) return []
    
    // Init result array and queue
    const result = []
    let queue = [root]

    while (queue.length) {
        let length = queue.length;
        let count = 0
        let currentNode;

        while (count < length) {
            // Grab currentNode out of beggining of queue
            currentNode = queue.shift()
            
            // Push child nodes into queue from left to right
            if (currentNode.left) queue.push(currentNode.left)
            if (currentNode.right) queue.push(currentNode.right)

            // Increment count
            count++
        }

        result.push(currentNode.value)
    }

    return result
};
