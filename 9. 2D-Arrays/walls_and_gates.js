const WALL = -1;
const GATE = 0;
const EMPTY = Infinity;

const directions = [
	[-1, 0],
	[0, 1],
	[1, 0],
	[0, -1],
];

const wallsAndGates = function (matrix) {
	for (let row = 0; row < matrix.length; row++) {
		for (let col = 0; col < matrix[0].length; col++) {
			if (matrix[row][col] === GATE) {
				dfs(matrix, row, col, 0);
			}
		}
	}

	return matrix;
};

const dfs = function (matrix, row, col, distance) {
	let rowLength = matrix.length;
	let colLength = matrix[0].length;
	if (row < 0 || row >= rowLength || col < 0 || col >= colLength || matrix[row][col] < distance) {
		return;
	}

	matrix[row][col] = distance;

	for (let i = 0; i < directions.length; i++) {
		const currentDir = directions[i];
		const nextRow = currentDir[0] + row;
		const nextCol = currentDir[1] + col;

		dfs(matrix, nextRow, nextCol, distance + 1);
	}
};
