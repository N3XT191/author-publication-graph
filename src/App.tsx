import React, { useState } from "react";
import ReactEcharts from "echarts-for-react";
import { css } from "glamor";
import { prepareData } from "./prepareData";
import GA4React from "ga-4-react";
const ga4react = new GA4React("G-HYL2XYL21Y");
ga4react.initialize().then(
	(ga4) => {
		ga4.pageview("path");
		ga4.gtag("event", "pageview", "path"); // or your custom gtag event
	},
	(err) => {
		console.error(err);
	}
);

const styles = {
	container: css({
		height: "100vh",
		width: "100vw",
	}),
	authorsContainer: css({
		paddingLeft: 100,
	}),
	title: css({ fontSize: 30, fontWeight: 500, paddingTop: 5, paddingBottom: 10 }),
	authors: css({
		fontSize: 20,
		display: "flex",
		flexFlow: "column wrap",
		padding: "3px",
		overflow: "auto",
		alignContent: "flex-start",
		maxHeight: "100px",
	}),
	author: css({
		width: "190px",
		marginRight: 10,
	}),
};

const preparedData = prepareData();
const option = (showAuthors: boolean[]) => {
	return {
		textStyle: { fontFamily: "Assistant, sans-serif" },
		color: [
			"#1f77b4",
			"#ff7f0e",
			"#2ca02c",
			"#d62728",
			"#9467bd",
			"#8c564b",
			"#e377c2",
			"#7f7f7f",
			"#bcbd22",
			"#17becf",
		],
		title: {
			text: "Publications of selected authors",
			left: "center",
			top: 10,
			textStyle: { fontSize: 35, fontWeight: 500 as 500 },
		},
		grid: {
			top: 60,
		},
		legend: {
			left: "12%",
			top: "12%",
			orient: "vertical" as "vertical",
			textStyle: {
				fontSize: 25,
			},
			borderWidth: 2,
			borderColor: "#666",
			backgroundColor: "#fff",
			icon: "roundRect" as "roundRect",
			itemHeight: 16,
			itemWidth: 45,
		},
		tooltip: {
			triggerOn: "mousemove|click" as "mousemove|click",
			hideDelay: 300,
			formatter: (
				params: any,
				ticket: string,
				callback: (ticket: string, html: string) => void
			) => {
				return (
					params.marker +
					params.seriesName +
					"<br/>" +
					params.data[3] +
					"<br/>" +
					Math.round(params.data[2] / 100) / 10 +
					"k words" +
					"<br/>" +
					"Published in " +
					new Date(params.data[0]).getFullYear()
				);
			},
			backgroundColor: "rgba(50,50,50,0.9)",
		},
		xAxis: {
			type: "time" as "time",
			max: "2022-01-01",
			axisLabel: {
				formatter: function (value: any) {
					return new Date(value).getFullYear();
				},
				fontSize: 20,
			},
			axisTick: {
				lineStyle: {
					width: 1.5,
				},
				length: 6.5,
			},
			splitNumber: 10,
			name: "Publication Date",
			nameLocation: "middle" as "middle",
			nameTextStyle: {
				fontSize: 31,
				padding: [15, 0, 0, 0],
			},
		},
		yAxis: {
			type: "value" as "value",
			axisLabel: {
				formatter: function (value: any) {
					return value / 1000000 + " M";
				},
				fontSize: 20,
			},
			axisTick: {
				lineStyle: {
					width: 1.5,
				},
				length: 6.5,
			},
			name: "Cummulative number of words published",
			nameLocation: "middle" as "middle",
			nameTextStyle: {
				fontSize: 31,
				padding: [0, 0, 35, 0],
			},
		},

		series: preparedData.filter((item, i) => showAuthors[i]),
	};
};
function App() {
	const [showAuthors, setShowAuthors] = useState(
		Array(preparedData.length)
			.fill(false)
			.map((a) => Math.random() < 0.5)
	);
	return (
		<div {...styles.container}>
			<div {...styles.authorsContainer}>
				<div {...styles.title}>Authors</div>
				<div {...styles.authors}>
					{preparedData.map((author, i) => (
						<div key={i} {...styles.author}>
							<input
								type="checkbox"
								checked={showAuthors[i]}
								onChange={(e) => {
									const newMask = [...showAuthors];
									newMask[i] = e.target.checked;
									setShowAuthors(newMask);
								}}
							/>
							{author.name + " "}
						</div>
					))}
				</div>
			</div>
			<ReactEcharts
				option={option(showAuthors)}
				notMerge={true}
				lazyUpdate={true}
				theme={"theme_name"}
				style={{ height: "750px" }}
			/>
		</div>
	);
}

export default App;
