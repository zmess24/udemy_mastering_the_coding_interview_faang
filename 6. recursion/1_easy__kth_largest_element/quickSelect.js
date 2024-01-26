/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

const quickSelect = function (array, left, right, indexToFind) {
	if (left < right) {
		const partitionIndex = partition(array, left, right);
		// QuickSort left side
		if (partitionIndex === indexToFind) {
			return array[partitionIndex];
		} else if (indexToFind < partitionIndex) {
			return quickSelect(array, left, partitionIndex - 1, indexToFind);
		} else {
			return quickSelect(array, partitionIndex + 1, right, indexToFind);
		}
	}
};

const partition = function (array, left, right) {
	const pivotElement = array[right];
	let paritionIndex = left;

	for (let j = left; j < right; j++) {
		if (array[j] < pivotElement) {
			swap(array, paritionIndex, j);
			paritionIndex++;
		}
	}

	swap(array, paritionIndex, right);
	return paritionIndex;
};
// Time: O(n)

const swap = function (array, i, j) {
	const temp = array[i];
	array[i] = array[j];
	array[j] = temp;
};

const findKthLargest = function (array, k) {
	const indexToFind = array.length - k;
	quickSelect(array, 0, array.length - 1, indexToFind);
	return array[indexToFind];
};

// Time: O(N)
// Space O(log(n))
