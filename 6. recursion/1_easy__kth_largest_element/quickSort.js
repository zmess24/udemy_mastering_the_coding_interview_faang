/**
|--------------------------------------------------
| Udemy Solution
|--------------------------------------------------
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

const quickSort = function (array, left, right) {
	if (left < right) {
		const partitionIndex = partition(array, left, right);
		// QuickSort left side
		quickSort(array, left, partitionIndex - 1);
		// QuickSort right side
		quickSort(array, partitionIndex + 1, right);
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

const swap = function (array, i, j) {
	const temp = array[i];
	array[i] = array[j];
	array[j] = temp;
};

const findKthLargest = function (array, k) {
	const indexToFind = array.length - k;
	quickSort(array, 0, array.length - 1);
	return array[indexToFind];
};

// Time: O(n log(n))
// Space O(log(n))
