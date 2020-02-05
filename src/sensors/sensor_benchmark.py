import time, random

from src.sensors.matomo_utils import valueFromAction, getDevices
from src.sensors.utils import end, sendDataToTipboard
from src.tipboard.app.properties import COLOR_TAB


def updateNormChartTipBoard(bench, tile, isTest=False):
    if not "values" in bench[0]:
        return
    print("je suis ici")
    datasetLength = len(bench)
    data = dict()
    data['title'] = dict(display=False)
    data['datasets'] = list()
    for index in range(datasetLength):
        data['datasets'].append(
            dict(label=bench[index]["device"],
                 data=bench[index]["values"],
                 borderColor=COLOR_TAB[index]))
    tipboardAnswer = sendDataToTipboard(data=data, tile_template='norm_chart', tile_id=tile, isTest=isTest)
    end(title=f'{tile} -> {tile}', start_time=time.time(), tipboardAnswer=tipboardAnswer, TILE_ID=tile)


def updateListingTipBoard(list, tile, isTest=False):
    data = {'items': list}
    tipboardAnswer = sendDataToTipboard(data=data, tile_template='norm_chart', tile_id=tile, isTest=isTest)
    end(title=f'{tile} -> {tile}', start_time=time.time(), tipboardAnswer=tipboardAnswer, TILE_ID=tile)


def updateCPUTipBoard(isTest=False):
    cpu_bench = valueFromAction("ackleyBenchmark")
    updateNormChartTipBoard(cpu_bench, 'cpu', isTest)


def updateGPUTipBoard(isTest=False):
    gpu_bench = valueFromAction("scroll")
    print(gpu_bench)
    updateNormChartTipBoard(gpu_bench, 'gpu', isTest)


def updateNetworkTipBoard(isTest=False):
    network_bench = valueFromAction("downloadFile")
    updateNormChartTipBoard(network_bench, 'network', isTest)


def updateDevicesTipBoard(isTest=False):
    list = getDevices()
    updateListingTipBoard(list, 'list_devices', isTest)


def sonde_bench(isTest=False):
    updateCPUTipBoard(isTest)
    updateGPUTipBoard(isTest)
    updateNetworkTipBoard(isTest)

    updateDevicesTipBoard(isTest)
