Background

We have discussed a lot about shapefile, ranging from how to get it, see shapefiles, and make their own shapefile. Now we will go into the discussion of editing shapefile.

contents

How to edit the shapefile geometry data is as follows:

Open python at the command prompt

import shapefile

sf = shapefile.Editor (shapefile = 'namafile.shp')

sf.point (19,19,0,0)

sf.record ('Record1', 'Record2')

sf.save ('filename')

How to remove the geometry data from shapefiles are as follows:

Open python at the command prompt

import shapefile

e = shapefile.Editor ('namafile.shp')

e.shape (1) -> to record how much

e.delete (1)

e.save ('filename')

Conclusions and recommendations

In my opinion, management shapefile using python can be fairly simple from syntax syntax used therefore highly recommended to use the python programming language as a shapefile management.
