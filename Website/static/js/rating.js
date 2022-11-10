


let trace1 = [{
    x: main_data.map(item => item.tournament),
    y: main_data.map(item => item.better_fifa_win),
    type: 'bar'
}];



let  trace2 = [{
        x: main_data.map(item => item.tournament),
        y: main_data.map(item => item.better_ea_team_win),
        type: 'bar'
}];

let dat = [trace1, trace2]




    
Plotly.newPlot("plot", dat)
