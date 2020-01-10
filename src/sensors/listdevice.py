import time, random
from src.sensors.utils import end, sendDataToTipboard, getTimeStr
import logging

NAME_OF_SENSORS = "listing"
TILE_TEMPLATE = "listing"
TILE_ID = "list_devices"


def getItemList():
    return {
        'items':
            [f'A50',
             f'A40',
             f'TC52'
             ]
    }


def executeScriptToGetData():
    return getItemList()


def sonde_listdevice(isTest=False):
    print(f"{getTimeStr()} (+) Starting sensors listdevice", flush=True)
    start_time = time.time()
    data = executeScriptToGetData()
    tipboardAnswer = sendDataToTipboard(data=data, tile_template=TILE_TEMPLATE, tile_id=TILE_ID, isTest=isTest)
    end(title=f"sensors list device -> {tipboardAnswer.text}", start_time=start_time, tipboardAnswer=tipboardAnswer,
        TILE_ID=TILE_ID)
