const ctx = document.getElementById("Tournament").getContext("2d)");

let delayed;

let gradient = ctx.createLinearGradient(0, 0, 0, 400);
gradient.addColorStop(0, "rgba(58,123,213,1");
gradient.addColorStop(1, "rgba(0,210,255, 0.3)");

const labels =[
    '2001',
    '2002',
];

const data = {
    labels,
    datasets:[
        {
        data:[500],
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

const Tournament = new Chart(ctx, config);