async function linearO(length) {
	function linear(length) {
		return new Promise((resolve, reject) => {
			let iterations = 0;
			for (let i = 0; i < length; i++) {
				iterations++;
			}
			resolve({ iterations, end: Date.now() });
		});
	}

	let start = Date.now();
	let { iterations, end } = await linear(length);
	return { iterations, elapsed: end - start };
}
