var trace = {
    x: data_js.map(item => item.date),
    y: y_data = data_js.map(item => item.goals_scored),
    type: 'line',
    transforms: [{
        type: 'groupby',
        groups: data_js.map(item => item.team),
        aggregations: [
            {target: 'y', func: 'cumsum', enabled: true},
          ]}]
};

Plotly.newPlot('myDiv', [trace])