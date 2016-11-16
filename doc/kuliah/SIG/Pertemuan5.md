Background
In previous meetings we have discussed shapefile and way of retrieving the data shapefile her, now we will discuss how to create shapefiles simple, in geospatial there are two types of data, ie vector and raster (discussed earlier) and shapefiles that we will create is a vector form , Let's get on with it.

Contents
Is a non shapefile format that is efficient and simple topology and serves as a storage container geometric location and attribute information from a geographic data. To make additions we shapefiles using python programming language and plugins pyshp.

How to create a shapefile using python:
'Import shapefile'
Incorporate variable initialization, a variable suppose to shapefile.writer it can be made with => 'a = shapefile.writer ()'
In mengcreate shapefile data, there are two formats used:
1. SHP => in SHP format, there are 3 types of shape file that is Point, Polyline and Polygon.
    Example: shp => a.point (x, y)

                                  a.poly [(x, y), (v, w)]

2. DBF => in DBF format there are three fields that are used. The first field contains the attributes of the table, while the second field contains the method used and the third field serves to save the shapefile name previously entered.
   Example: dbf => a.field ( 'name.field', 'c', '40')
        a.record ( 'bdg')

Geospatial data is stored using a method a.save ( 'file.shp').
Explanation of methods used:
Point (x, y): insert data in the form of paint into shp and all data must be formatted ESRI.1
Poly [(a, b), (c, d)]: polygon-shaped insert geospatial data (back to the starting point) or polyline (not back to point early).
Field ( 'name', 'c', '40'): it means making the polygon attribute table 'name' with varchar data type with a length of 40. This method can be repeated and can be done for kebuthan new field again.
Record ( 'Bandung'): fill the table with only one field value 'Bandung'.
Save ( 'nama.file'): save file to save the file.
How to add the Record:

On Point = 'a.point (x, y)' or 'a.point (x, y, 0,0)' with domain x and y are the coordinates
On polyline = 'a.poly (shapefile = 3 parts = [[[x1, y1, z1, w1], [x2, y2, z2, w2], [......]]])'
In Polygon = 'a.poly) shapefile = 5, parts = [[[.......], [.......]]])'

Conclusions and recommendations
With python as a means of making shapefiles, then we can understand how technical shapefile of manufacture is simple, once understood, we certainly would be easier to understand the characteristics of a good shapefile of Natural Earth and from that we created.
