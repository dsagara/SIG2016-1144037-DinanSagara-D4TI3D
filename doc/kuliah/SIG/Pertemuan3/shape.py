#!/bin/python

import shapefile
sf = shapefile.Reader("D:\cultural\\ne_10m_admin_0_countries.shp")
shapes = sf.shapes()
len(shapes)

#for name in dir(shape[3]);
#		if not name.startswitch('__');
#				print name