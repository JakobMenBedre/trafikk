
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PornHub</title>
    <script type="text/javascript" src="kon.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
    integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
    crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
        integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
        crossorigin=""> </script>
    <link rel="fugu konge.png" type="image/x-icon" href="fugu konge.png">

</head>
<body>
        <div id="map" style="width: 900px; height: 912px; position: relative;" class="leaflet-container leaflet-touch leaflet-fade-anim leaflet-grab leaflet-touch-drag leaflet-touch-zoom" tabindex="0">
        <script>

            var varlong = sessionStorage.getItem("varlong");
            var varlat = sessionStorage.getItem("varlat");
            console.log(varlong);
            console.log(varlat);
            const map = L.map('map').setView([varlat, varlong], 13);
    
            const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(map);
    
            L.marker([varlat, varlong]).addTo(map)
                .bindPopup('IP:'+ domain +  "<br>, Country:" + varea)
                .openPopup();
            $.get('/path/to/script.php', payload, function(response) {
    alert('Sent the values!');
});
        </script>
    
            
        </div>




    
    
</body>
</html>