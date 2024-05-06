// Do not edit the class below except
// for the breadthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
	constructor(name) {
		this.name = name;
		this.children = [];
	}

	addChild(name) {
		this.children.push(new Node(name));
		return this;
	}

	breadthFirstSearch(array) {
		const queue = [this];
		const seen = new Set();

		while (queue.length) {
			const currentNode = queue.shift();
			array.push(currentNode.name);
			seen.add(currentNode.name);

			for (let i = 0; i < currentNode.children.length; i++) {
				let connection = currentNode.children[i];
				if (!seen.has(connection.name)) {
					queue.push(connection);
				}
			}
		}

		return array;
	}
}

// Do not edit the line below.
exports.Node = Node;
