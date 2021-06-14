# -*- coding: utf-8 -*-
import yaml
import requests

class RemoApi:
    def __init__(self, settingfile = 'setting.yml') -> None:
        with open('setting.yml') as file:
            stng = yaml.safe_load(file)
        self.stng = stng

    def getTemp(self):
        stng = self.stng
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer %s'%stng['token'],
            }
        response = requests.get('https://api.nature.global/1/devices', headers=headers, verify=False)
        newest_events = response.json()[0]['newest_events']
        return {'datetime' : newest_events['te']['created_at'], 'temp' : newest_events['te']['val']}

#remo = RemoApi()
#remores = remo.getTemp()
#print(remores['datetime'])

