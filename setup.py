# -*- coding: utf-8 -*-
import yaml
import requests
import sqlite3

dbname = "roomtemp.db"
connector = sqlite3.connect(dbname)
cursor = connector.cursor()

sql = """
CREATE TABLE "temp" (
"ID" INTEGER PRIMARY KEY ASC AUTOINCREMENT,
"datetime" TEXT,
"created" TEXT,
"temp" REAL
);
"""
connector.execute(sql)
connector.commit()
connector.close()

stoken = input('Enter the token : ') 
yml = {'token': '%s'%stoken}
with open('setting.yml', 'w') as file:
    yaml.dump(yml, file)

with open('setting.yml') as file:
    stng = yaml.safe_load(file)
    print(stng)

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer %s'%stng['token'],
}

response = requests.get('https://api.nature.global/1/devices', headers=headers, verify=False)

#print(response)
print(response.json())
print(response.json()[0]['newest_events'])


response = requests.get('https://api.nature.global/1/appliances', headers=headers, verify=False)
print(response.json())