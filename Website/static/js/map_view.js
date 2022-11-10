// Leaflet map
var map = L.map('map', {
  center: [21.505, -0.09],
  zoom: 3,
  noWrap: true,
  reuseTiles: true
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var url = 'http://127.0.0.1:5000/api/map_data_count';

d3.json(url).then(function(response) {

  console.log(response);

  var heatArray = [];

  for (var i = 0; i < response.length; i++) {
    var location = response[i];

    if (location) {
      heatArray.push([location.lat, location.long]);
    }
  }

  var heat = L.heatLayer(heatArray, {
    radius: (location.count*6),
    blur: 20,
    maxZoom: 8,
    max: 1,
    gradient: {
      0.0: 'green',
      0.5: 'yellow',
      1.0: 'red'
    }
  }).addTo(map);
});
// Plotly bar
var url = 'http://127.0.0.1:5000/api/bardata';

d3.json(url).then(function(response) {

  console.log(response);

  var x = [];
  var y = [];

  for (var i = 0; i < response.length; i++) {
    var location = response[i];

    if (location) {
      x.push(location.team);
      y.push(location.count);
    }
  }

  var data = [
    {
      x: x,
      y: y,
      type: 'bar',
      marker: {
        color: 'rgb(158,202,225)',
        line: {
          color: 'rgb(8,48,107)',
          width: 1.5
    }}}
  ];

  var layout = {
    title: {text:'World Cup Games Played', font:{size:24}},
    yaxis: {title:'Count of Games', font:{size:24}},
    xaxis: {tickangle:28}
  }

  var config = {responsive: true};

  Plotly.newPlot('bar', data, layout, config);
});
