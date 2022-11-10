
const ctx =document.getElementById('myChart');

let delayed;

let gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
gradient.addColorStop(0, Utils.CHART_COLORS.blue);
gradient.addColorStop(0.5, Utils.CHART_COLORS.yellow);
gradient.addColorStop(1, Utils.CHART_COLORS.red);

const labels = main_data.map(item =>item.date)

const data = {
    labels,
    datasets:[
        {
        data:['Afghanistan','Asia','Albania', 'Europe', 'Algeria', 'Africa', 'American Samoa', 'Oceania', 'Andorra','Angola', 'Anguilla', 'North America', 'South America'],
        label: "Goals Scored",
        fill: true,
        backgroundColor: gradient,
        borderColor: "#fff",
        pointBackgroundColor: "#fff"
        
    },
 ],
};

const config = {
    type: 'line',
    data: data,
    option:{
        radius: 5,
        responsive: true,
        animation:{
            onComplete: () => {
                delayed = true;
            },
        delay:(context) => {
            let delay = 0;
            if(context.type === "data" && context.mode ==="default" && !delayed) {
                delay = context.dataIndex * 300 + context.datasetIndex * 100;
            }
            return delay;
        },
    },

    },
};

const myChart = new Chart(ctx, config);