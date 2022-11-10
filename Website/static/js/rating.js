


    
let trace = [{
    x: main_data.map(item => item.tournament),
    y: main_data.map(item => item.better_fifa_win),
    type: 'bar'
}];

Plotly.newPlot('myChart', trace)

let trace2 = [{
        x: main_data.map(item => item.tournament),
        y: main_data.map(item => item.better_ea_team_win),
        type: 'bar'
}];


    
Plotly.newPlot('myChart2', trace2)