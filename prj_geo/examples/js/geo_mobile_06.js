var ini_lat = 25.746114,
    ini_lon = -100.197024;
var locationCircle ;            

var map     = L.map('map').fitWorld();

var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

var myMarker = L.marker([ ini_lat, ini_lon ], {title: "MyPoint", alt: "The Big I", draggable: true})
    .addTo(map)
    .on('dragend', function(event) {
        var latlng = event.target.getLatLng();
        locationCircle.setLatLng( latlng );
        typePosition( latlng );
        });
    
// type the GeoLocation, the coordinates in the hidden fields.            
function typePosition( latlng ){
    var txt_latlng      = document.getElementById( "txt_latlng"    );
    var txt_latitude    = document.getElementById( "txt_latitude"  );
    var txt_longitude   = document.getElementById( "txt_longitude" );
    txt_latlng   .value = latlng;
    txt_latitude .value = latlng.lat;
    txt_longitude.value = latlng.lng;
}

function onLocationFound(e) {
    var radius     = e.accuracy / 2;
    locationCircle = L.circle(e.latlng, radius).addTo(map);
    myMarker.setLatLng([e.latlng.lat, e.latlng.lng]).update(); 
    typePosition( e.latlng );
}

function onLocationError(e) {
    alert(e.message);
}

map.on('locationfound', onLocationFound);
map.on('locationerror', onLocationError);
map.locate( { setView: true, maxZoom: 18 });
