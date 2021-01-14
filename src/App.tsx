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
		width: "100%",
		display: "flex",
		flexDirection: "column",
		alignItems: "center",
	}),
	title: css({ fontSize: 30, fontWeight: 500, paddingTop: 5, paddingBottom: 10 }),
	authors: css({
		fontSize: 20,
		display: "flex",
		flexWrap: "wrap",
		flexDirection: "column",
		padding: "3px",
		alignContent: "center",
		overflow: "scroll",
		maxHeight: "100px",
		width: "100%",
		maxWidth: "100%",
		"@media(max-width: 600px)": {
			maxHeight: "100%",
		},
	}),
	author: css({
		width: "190px",
		marginRight: 10,
		cursor: "pointer",
	}),
};

const preparedData = prepareData();
const option = (showAuthors: boolean[], mobile: boolean) => {
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
			textStyle: { fontSize: mobile ? 20 : 35, fontWeight: 500 as 500 },
		},
		grid: {
			top: mobile ? 40 : 60,
			left: mobile ? 75 : 100,
			right: mobile ? 12 : 25,
		},
		legend: {
			left: mobile ? 80 : 110,
			top: mobile ? 45 : 70,
			orient: "vertical" as "vertical",
			textStyle: {
				fontSize: mobile ? 15 : 25,
			},
			borderWidth: mobile ? 1 : 2,
			borderColor: "#666",
			backgroundColor: "#fff",
			icon: "roundRect" as "roundRect",
			itemHeight: mobile ? 10 : 16,
			itemWidth: mobile ? 28 : 45,
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
				fontSize: mobile ? 14 : 20,
			},
			axisTick: {
				lineStyle: {
					width: 1.5,
				},
				length: mobile ? 3 : 6.5,
			},
			splitNumber: mobile ? 5 : 10,
			name: "Publication Date",
			nameLocation: "middle" as "middle",
			nameTextStyle: {
				fontSize: mobile ? 20 : 31,
				padding: [15, 0, 0, 0],
			},
		},
		yAxis: {
			type: "value" as "value",
			axisLabel: {
				formatter: function (value: any) {
					return value / 1000000 + " M";
				},
				fontSize: mobile ? 14 : 20,
			},
			axisTick: {
				lineStyle: {
					width: 1.5,
				},
				length: mobile ? 3 : 6.5,
			},
			name: "Cummulative number of words published",
			nameLocation: "middle" as "middle",
			nameTextStyle: {
				fontSize: mobile ? 20 : 31,
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
	console.log(window.screen.width);
	return (
		<div {...styles.container}>
			<div {...styles.authorsContainer}>
				<div {...styles.title}>Authors</div>
				<div {...styles.authors}>
					{preparedData.map((author, i) => (
						<div
							key={i}
							{...styles.author}
							onClick={(e) => {
								const newMask = [...showAuthors];
								newMask[i] = !showAuthors[i];
								setShowAuthors(newMask);
							}}
						>
							<input type="checkbox" checked={showAuthors[i]} />
							{author.name + " "}
						</div>
					))}
				</div>
			</div>
			<ReactEcharts
				option={option(showAuthors, window.innerWidth! < 700)}
				notMerge={true}
				lazyUpdate={true}
				theme={"theme_name"}
				style={{
					height: "100%",
					maxHeight: "750px",
					width: "100%",
				}}
			/>
		</div>
	);
}

export default App;
