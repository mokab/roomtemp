# -*- coding: utf-8 -*-
import schedule
import time
import sqlite3
import RemoApi

remo = RemoApi.RemoApi()
dbname = "roomtemp.db"

def job():
    remores = remo.getTemp()
    print(remores['datetime'])
    connector = sqlite3.connect(dbname)
    cursor = connector.cursor()

    sql = """
    insert into 
    temp(datetime, created, temp) 
    values(datetime(datetime(),"localtime"), "%s", %f);
    """
    connector.execute(sql%(remores['datetime'], remores['temp']))
    connector.commit()
    connector.close()

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

