

// var data = team_data

// // create the chart and set the data
// chart = anychart.heatMap(data);

// // set the chart title
// chart.title("Human Development Index by region (2010-2018)");

// // create and configure the color scale.
// var customColorScale = anychart.scales.linearColor();
// customColorScale.colors(["#ACE8D4", "#00726A"]);

// // set the color scale as the color scale of the chart
// chart.colorScale(customColorScale);

// // set the container id
// chart.container("container");

// // initiate drawing the chart
// chart.draw();
var data = [
    {
      z: [3,2,3,4],
      x: [1993,1992,1993,1994],
      y: ['A', 'B', 'C', 'D'],
      type: 'heatmap',
      hoverongaps: false
    }
  ];
  
  Plotly.newPlot('myDiv', data);