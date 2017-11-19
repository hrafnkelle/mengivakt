# About
Scripts and config for a raspberry pi with a camera to monitor
* Temperature via w1 ds18b20 sensors and log to thingspeak
* take a photo and possibly upload to dropbox

(c) 2017 Hrafnkell Eiríksson


# Setup

* Set up incrond (if you want to upload to dropbox)
* Set up daemon so raspistill can be run as a daemon from crontab
* add to crontab from the crontabfile
* set up a ramdisk by adding to fstab
* set up a few python3 modules
   * ephem (for calculating if sun is above/below horzon)
   * dropbox (for uploading images)
* Install pagekite (http://pagekite.net) and expose your webserver and ssh (if you want to)
* symlink /var/ramdisk/pic.jpg to /var/www/html/pic.jpg
* symlink the index.html file in this repository to /var/www/html/index.html
* Add to rc.local to turn off the rpi leds that might interfere with long exposure times
```bash
echo none > /sys/class/leds/led0/trigger
echo none > /sys/class/leds/led1/trigger
echo 0 > /sys/class/leds/led10brightness
echo 0 > /sys/class/leds/led1/brightness
```
* Create a configUpload.py file with the following configuration
```python
access_token='YOURDROPBOXTOKEN'
thingspeakkey='YOURTHINGSPEAKKEY'
obs_lat, obs_lon = 'YOUR.LATITUDE','YOUR.LONGDITUDE'
```

