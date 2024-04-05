// Import Leaflet library
import L from 'leaflet';

// Initialize the map
var map = L.map('map').setView([51.505, -0.09], 13);

// Add the base tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add a marker to the map
var marker = L.marker([51.5, -0.09]).addTo(map);

// Add a popup to the marker
marker.bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();
