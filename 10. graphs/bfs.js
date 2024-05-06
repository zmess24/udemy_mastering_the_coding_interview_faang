function bfs_graph(graph) {
	const queue = [0];
	const values = [];
	const seen = {};

	while (queue.length) {
		const vertex = queue.shift();
		values.push(vertex);
		seen[vertex] = true;

		const connections = graph[vertex];

		for (let i = 0; i < connection.length; i++) {
			if (!seen[connection[i]]) {
				queue.push(connection[i]);
			}
		}
	}
}
