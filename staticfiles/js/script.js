// Coordonnées de Sfax
var sfaxLat = 34.7404;
var sfaxLng = 10.7605;

// Initialisation de la carte centrée sur Sfax
var map = L.map('map').setView([sfaxLat, sfaxLng], 12); // Coordonnées de Sfax

// Ajouter une carte OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Marqueur pour le point de départ
var markerStart = null;
// Marqueur pour le point d'arrivée
var markerEnd = null;

// Fonction pour mettre à jour les coordonnées dans les champs
function updateCoordinates(lat, lng, isStart) {
    if (isStart) {
        document.getElementById('start-lat').value = lat;
        document.getElementById('start-lng').value = lng;
    } else {
        document.getElementById('end-lat').value = lat;
        document.getElementById('end-lng').value = lng;
    }
}

// Fonction pour effacer ou déplacer les marqueurs
function resetMarker(marker, isStart) {
    if (marker) {
        map.removeLayer(marker); // Supprime le marqueur de la carte
    }
    if (isStart) {
        document.getElementById('start-lat').value = '';
        document.getElementById('start-lng').value = '';
    } else {
        document.getElementById('end-lat').value = '';
        document.getElementById('end-lng').value = '';
    }
}

// Gestion du clic sur la carte pour ajouter un marqueur
map.on('click', function(e) {
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;

    // Ajouter ou déplacer un marqueur pour le point de départ
    if (!markerStart) {
        markerStart = L.marker([lat, lng]).addTo(map);
        markerStart.bindPopup("<b>Point de départ</b>").openPopup();
        updateCoordinates(lat, lng, true);
    }
    // Ajouter ou déplacer un marqueur pour le point d'arrivée
    else if (!markerEnd) {
        markerEnd = L.marker([lat, lng]).addTo(map);
        markerEnd.bindPopup("<b>Point d'arrivée</b>").openPopup();
        updateCoordinates(lat, lng, false);
    }
    // Si les deux marqueurs existent déjà, on déplace le point d'arrivée
    else {
        markerEnd.setLatLng(e.latlng);
        updateCoordinates(lat, lng, false);
    }
});

// Fonction pour effacer ou déplacer les marqueurs
document.getElementById('remove-start').addEventListener('click', function() {
    if (markerStart) {
        resetMarker(markerStart, true); // Supprimer le marqueur de départ
        markerStart = null; // Réinitialiser la variable de marqueur
    }
});

document.getElementById('remove-end').addEventListener('click', function() {
    if (markerEnd) {
        resetMarker(markerEnd, false); // Supprimer le marqueur d'arrivée
        markerEnd = null; // Réinitialiser la variable de marqueur
    }
});
