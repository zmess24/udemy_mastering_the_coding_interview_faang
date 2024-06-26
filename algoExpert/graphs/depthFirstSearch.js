// Do not edit the class below except
// for the depthFirstSearch method.
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

	depthFirstSearch(array, seen = new Set()) {
		if (!seen.has(this.name)) {
			array.push(this.name);
			seen.add(this.name);
		}

		for (const connection of this.children) {
			connection.depthFirstSearch(array, seen);
		}

		return array;
	}
}

// Do not edit the line below.
exports.Node = Node;
