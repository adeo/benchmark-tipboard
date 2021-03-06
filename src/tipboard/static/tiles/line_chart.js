

/**
 * Update for tile cumulative_flow & line_chartjs
 * @param data
 * @param tileType fillDataset = True || False => CumulativeFlow
 * @returns
 */
function updateDataset(data, tileType) {
    const predefinedLabel = ["label1", "label2", "label3", "label4", "label5"];
    const predefinedSeries = ["serie1", "serie2", "serie3", "serie4", "serie5"];
    let listOfDataset = [];
    let rcx = 0;
    $.each(data.datasets, function (index, dataset) {
        let datasetTmp = {
            label: ("label" in dataset) ? dataset.label : predefinedLabel[rcx],
            data: ("data" in dataset) ? dataset.data : [],
            fill: (tileType === "cumulative_flow"),
            backgroundColor: ("backgroundColor" in dataset) ?
                dataset.backgroundColor : Tipboard.Palette.tabColor[rcx],
            borderColor: ("backgroundColor" in dataset) ?
                dataset.backgroundColor : Tipboard.Palette.tabColor[rcx],
        };
        if (tileType === "cumulative_flow") {
            datasetTmp.trendlineLinear = {"lineStyle": "dotted", "width": 2}
        } else {
            delete datasetTmp.backgroundColor
        }
        listOfDataset.push(datasetTmp);
    });
    console.log(listOfDataset);
    return {
        labels: ("labels" in data) ? data.labels : predefinedSeries,
        datasets: listOfDataset,
    };
}


/**
 * update the line_chart tile & the cummulative_flow tile
 * @param tileId
 * @param data
 * @param meta
 * @param tileType
 */
function updateTileLinejs(tileId, data, meta, tileType) {
    console.log("line_chartjs::updateTile::start" + tileId);
    let chartId = `${tileId}-chart`;
    if (chartId in Tipboard.chartJsTile) {
        Tipboard.Dashboard.updateDataOfChartJS(Tipboard.chartJsTile[chartId],
            updateDataset(data, tileType));
    } else {
        let chart = document.getElementById(chartId);
        meta.options.title = getTitleForChartJSTitle(data);
        chart.parentElement.style.paddingBottom = "8%";
        Tipboard.chartJsTile[chartId] = new Chart(chart, {
            type: "line",
            data: updateDataset(data, tileType),
            options: meta.options
        });
    }
    console.log("linejs::type(" + tileType + ")::updateTile " + tileId);
}

Tipboard.Dashboard.registerUpdateFunction("line_chart", updateTileLinejs);
