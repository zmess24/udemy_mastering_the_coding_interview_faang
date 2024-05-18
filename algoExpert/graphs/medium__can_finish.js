// https://leetcode.com/problems/course-schedule/

/**
|--------------------------------------------------
| BFS
|--------------------------------------------------
*/

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
const canFinish = function (n, prerequisites) {
	const adjList = new Array(n).fill(0).map(() => []);

	for (let i = 0; i < prerequisites.length; i++) {
		const pair = prerequisites[i];
		adjList[pair[1]].push(pair[0]);
	}

	for (let v = 0; v < n; v++) {
		const queue = [];
		const seen = {};
		for (let i = 0; i < adjList[v].length; i++) {
			queue.push(adjList[v][i]);
		}

		while (queue.length) {
			const current = queue.shift();
			seen[current] = true;

			if (current === v) return false;
			const adjacent = adjList[current];
			for (let i = 0; i < adjacent.length; i++) {
				const next = adjacent[i];
				if (!seen[next]) {
					queue.push(next);
				}
			}
		}
	}

	return true;
};

/**
|--------------------------------------------------
| Topological Sort
|--------------------------------------------------
*/

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
const canFinish2 = function (n, prerequisites) {
	const inDegree = new Array(n).fill(0);
	const adjList = inDegree.map(() => []);

	for (let i = 0; i < prerequisites.length; i++) {
		const pair = prerequisites[i];
		inDegree[pair[0]]++;
		adjList[pair[1]].push(pair[0]);
	}

	const stack = [];

	for (let i = 0; i < inDegree.length; i++) {
		if (inDegree[i] === 0) {
			stack.push(i);
		}
	}

	let count = 0;

	while (stack.length) {
		const current = stack.pop();
		count++;

		const adjacent = adjList[current];

		for (let i = 0; i < adjacent.length; i++) {
			const next = adjacent[i];
			inDegree[next]--;
			if (inDegree[next] === 0) {
				stack.push(next);
			}
		}
	}

	return count === n;
};
