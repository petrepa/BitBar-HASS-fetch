#!/usr/bin/env python3

import requests
import sys, json

# User setting. Overwrite with your own. See README.md
SETTINGS = {
    # The entities you want to have in you menu bar
    # Change the name to something preferable, and fill in your entity id
    'entities': {
        'sensor1_name': ['sensor.1'],
        'sensor2_name': ['sensor.2'],
        'sensor3_name': ['sensor.3']
    },

    # Your remote access Home Assistant URL
    'url_params': {
        'remote_url': ['<UR_NABU_CASA_URL>'],
        'api_call': ['api/states/']
    },

    # Your long lived access token
    'token': {
        'Authorization': 'Bearer <YOUR_LONG_LIVED_ACCESS_TOKEN>',
    },
    
    # Other config elements
    'config': {
        # friendly name for elements (True/False)
        'fn_header_element': 'False',
        'fn_menu_elements': 'True'
    }
}

first = True

for i in SETTINGS['entities']:
    link = ''.join(SETTINGS['url_params']['remote_url']+SETTINGS['url_params']['api_call'] + SETTINGS['entities'][i])

    response = requests.request('GET', link, headers=SETTINGS['token'])
    response_str = json.loads(response.text)

    if first == True:
        if SETTINGS['config']['fn_header_element'] == 'False':
            print(response_str['state'] + response_str['attributes']['unit_of_measurement'])
        else:
            print(response_str['attributes']['friendly_name'] + ": " + response_str['state'] + response_str['attributes']['unit_of_measurement'])
        
        print('---')

        first = False
    else:
        if SETTINGS['config']['fn_menu_elements'] == 'False':
            print(response_str['state'] + response_str['attributes']['unit_of_measurement'])
        else:
            print(response_str['attributes']['friendly_name'] + ": " + response_str['state'] + response_str['attributes']['unit_of_measurement'])


