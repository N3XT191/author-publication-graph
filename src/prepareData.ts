import { data } from "./data";

const makeCumulativeData = (data: any[]) => {
	const newData = [] as any[];
	data.forEach((row: any) => {
		if (newData.length === 0) {
			newData.push([row[0], row[1], row[1], row[2]]);
		} else {
			newData.push([row[0], newData[newData.length - 1][1] + row[1], row[1], row[2]]);
		}
	});
	return newData;
};

function findLineByLeastSquares(values_x: any[], values_y: any[]) {
	values_x = values_x.map((val) => new Date(val).getTime());
	var sum_x = 0;
	var sum_y = 0;
	var sum_xy = 0;
	var sum_xx = 0;
	var count = 0;

	/*
	 * We'll use those variables for faster read/write access.
	 */
	var x = 0;
	var y = 0;
	var values_length = values_x.length;

	if (values_length !== values_y.length) {
		throw new Error("The parameters values_x and values_y need to have same size!");
	}

	/*
	 * Nothing to do.
	 */
	if (values_length === 0) {
		return [[], []];
	}

	/*
	 * Calculate the sum for each of the parts necessary.
	 */
	for (var v = 0; v < values_length; v++) {
		x = values_x[v];
		y = values_y[v];
		sum_x += x;
		sum_y += y;
		sum_xx += x * x;
		sum_xy += x * y;
		count++;
	}

	/*
	 * Calculate m and b for the formular:
	 * y = x * m + b
	 */
	var m = (count * sum_xy - sum_x * sum_y) / (count * sum_xx - sum_x * sum_x);
	var b = sum_y / count - (m * sum_x) / count;

	let y1 = 0;
	let x1 = (y1 - b) / m;

	let x2 = new Date("2022/01/01").getTime();
	let y2 = m * x2 + b;

	if (x1 < values_x[0]) {
		x1 = values_x[0] + 1000  * 360 * 24 * 5;
		y1 = m * x1 + b;
	}
	if (y2 > values_y[values_y.length - 1]) {
		y2 = values_y[values_y.length - 1];
		x2 = (y2 - b) / m;
	}
	if (y1 < 0 || y2 < 0) {
		console.log(y1, y2);
	}
	const coord1 = [new Date(x1).toISOString().split("T")[0], y1];
	const coord2 = [new Date(x2).toISOString().split("T")[0], y2];

	const coords = [coord1, coord2];

	console.log(coords);
	return coords;
}

function transpose(matrix: any) {
	return Object.keys(matrix[0]).map((colNumber) =>
		matrix.map((rowNumber: any) => rowNumber[colNumber])
	);
}

export const prepareData = () => {
	return data.map((author, i) => {
		const cumulativeData = makeCumulativeData(author.data);
		const transposedData = transpose(cumulativeData);
		const coords = findLineByLeastSquares(transposedData[0], transposedData[1]);
		return {
			name: author.name,
			zlevel: i,
			animationDuration: 500,
			type: "line",
			smooth: false,
			symbolSize: 10,
			sampling: "average",
			itemStyle: {
				borderWidth: 3,
				opacity: 1,
			},
			lineStyle: {
				width: 4.5,
			},
			data: cumulativeData,
			markLine: {
				symbol: "none" as "none",
				lineStyle: { width: 2 },
				data: [
					[
						{
							name: "",
							coord: coords[0],
						},
						{
							coord: coords[1],
						},
					],
				],
				silent: true,
			},
		};
	});
};
