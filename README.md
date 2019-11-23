# BitBar-HASS-fetch
Simple BitBar plugin using the Home Assistant API to put your desired sensor values from your home in the Mac status bar.

![Screenshot](https://github.com/petrepa/BitBar-HASS-fetch/blob/master/screenshot.png)

You can select as many sensor values as you want, and can configure if you want the friendly name as prefix or not.

## Installation
Install [BitBar](https://getbitbar.com/)

Copy HA_fetch.py to your BitBar directory.

Remember to make the script runable with the command
```
$ chmod +x HA_fetch.py
```
Edit the file and put in your remote access url, along with a long lived access token (created in your Home Assistant profile).

Configure your entity list to include the entities you want to show.

Example:
```
'entities': {
        'temperature': ['sensor.netatmo_ute_temperature'],
        'humidity': ['sensor.netatmo_ute_humidity'],
        'light_level': ['sensor.peter_lightlevel']
    },
```
This gives the result shown in the screenshot above.
