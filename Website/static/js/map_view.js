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
    radius: (location.count**2),
    blur: 5,
  }).addTo(map);

});