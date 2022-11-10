var data =


var trace = [{
    x: main_data.map(item => item.tournament),
    y: main_data.map(item => item.better_fifa_win),
    type: 'bar'
}];

Plotly.newPlot("MyChart", trace);


var  trace2 = [{
        x: main_data.map(item => item.tournament),
        y: main_data.map(item => item.better_ea_team_win),
        type: 'bar'
}];

Plotly.newPlot("MyChart2", trace);






    
Plotly.newPlot("plot", dat)
