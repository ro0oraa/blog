


var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var marker = L.marker([51.5, -0.09]).addTo(map);

function onMapClick(e) {
     
      var marker = L.marker(e.latlng).addTo(map);
      if (confirm("save to database") == true)
      {
      $.ajax({
        type: "POST",
        url: "/save_lang",
        data: JSON.stringify(e.latlng),
        contentType: "application/json",
        dataType: 'json' 
      })
    }
    else{}
  }
  
  map.on('click', onMapClick);


  {%for lan in langs%}
  var marker = L.marker({{lan.l1}},{{lan.l2}}).addTo(map);
  {%endfor%}