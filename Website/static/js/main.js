
const ctx =document.getElementById('myChart');

let delayed;

let gradient = ctx.createLinearGradient(0, 0, 0, 400);
gradient.addColorStop(0, "rgba(58,123,213,1");
gradient.addColorStop(1, "rgba(0,210,255, 0.3)");

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