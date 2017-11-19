#!/usr/bin/python3
import ephem
import math
import uploadConfig as cfg
sun = ephem.Sun()
obs = ephem.Observer()
obs.lat, obs.lon = cfg.obs_lat, cfg.obs_lon
obs.date = ephem.now()
sun.compute(obs)
print(math.degrees(float(sun.alt)))
print(math.degrees(float(sun.az)))
print(obs.date)
if math.degrees(float(sun.alt))>-7:
    exit(1)
else:
    exit(0)
