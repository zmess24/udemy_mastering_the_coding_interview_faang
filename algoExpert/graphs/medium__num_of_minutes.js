/**
 * @param {number} n
 * @param {number} headID
 * @param {number[]} manager
 * @param {number[]} informTime
 * @return {number}
 */
var numOfMinutes = function (n, headID, managers, informTime) {
	const adjList = managers.map(() => []);

	for (let employee = 0; employee < n; employee++) {
		const manager = managers[employee];
		if (manager === -1) continue;
		adjList[manager].push(employee);
	}

	return dfs(headID, adjList, informTime);
};

const dfs = function (currentID, adjList, informTime) {
	if (adjList[currentID].length === 0) return 0;
	let max = 0;
	const subordinates = adjList[currentID];

	for (let i = 0; i < subordinates.length; i++) {
		max = Math.max(max, dfs(subordinates[i], adjList, informTime));
	}

	return max + informTime[currentID];
};
