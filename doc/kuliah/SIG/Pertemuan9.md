Web services for spatial data enable using data from servers directly with desktop GIS software, without downloading first data as files to the own computer. In such a way it is possible to use always up-to-date data easily. All most common commercial and open source GIS desktop software products support web standards (MapInfo, ArcGIS, QGIS, GRASS etc.). Web services are used so, that the user connects to the service using a special menu. For connection user needs to know the server's URL. After connecting to the server, the user gets a list of available map layers. Web services are also easy to use in map applications on web. Data may be requested also directly with a http GET or POST request.

The most common web service standards are Open GeoSpatial Consortium's (OGC):

WMS (Web Map Service)
WMTS (Web Map Tile Service)
WFS (Web Feature Service)
WCS (Web Coverage Service).
WMS and WMTS service return map image in raster format, WFS data in vector format, WCS data in raster format. In WMTS services maps are available only in pre-defined scales and size. In WMS services scale and map size can be set without restrictions. WMTS services are faster, because often the map tiles are already ready at the server. For requesting only part of data different filters may be used, for example BBOX defines the area of interest.
