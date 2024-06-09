// https://leetcode.com/problems/rotting-oranges/description/

var orangesRotting = function (grid) {
	if (grid.length === 0) return 0;

	const directions = [
		[-1, 0],
		[0, 1],
		[1, 0],
		[0, -1],
	];
	// Constants = orange states
	const ROTTEN = 2;
	const FRESH = 1;
	const EMPTY = 0;

	const queue = [];
	let freshOranges = 0;

	for (let row = 0; row < grid.length; row++) {
		for (let col = 0; col < grid[0].length; col++) {
			if (grid[row][col] === ROTTEN) {
				queue.push([row, col]);
			}

			if (grid[row][col] === FRESH) {
				freshOranges++;
			}
		}
	}

	let currentQueueSize = queue.length;
	let minutes = 0;

	while (queue.length > 0) {
		if (currentQueueSize === 0) {
			minutes++;
			currentQueueSize = queue.length;
		}

		const currentOrange = queue.shift();
		currentQueueSize--;
		const row = currentOrange[0];
		const col = currentOrange[1];

		for (let i = 0; i < directions.length; i++) {
			const currentDir = directions[i];
			const nextRow = currentDir[0] + row;
			const nextCol = currentDir[1] + col;

			if (nextRow < 0 || nextRow >= grid.length || nextCol < 0 || nextCol >= grid[0].length) {
				continue;
			}

			if (grid[nextRow][nextCol] === FRESH) {
				grid[nextRow][nextCol] = 2;
				freshOranges--;
				queue.push([nextRow, nextCol]);
			}
		}
	}

	if (freshOranges > 0) {
		return -1;
	}

	return minutes;
};
