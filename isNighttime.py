#!/usr/bin/python3
import ephem
import math
import uploadConfig as cfg
sun = ephem.Sun()
midengi = ephem.Observer()
midengi.lat, midengi.lon = cfg.midengi_lat, cfg.midengi_lon
midengi.date = ephem.now()
sun.compute(midengi)
print(math.degrees(float(sun.alt)))
print(math.degrees(float(sun.az)))
print(midengi.date)
if math.degrees(float(sun.alt))>-7:
    exit(1)
else:
    exit(0)
