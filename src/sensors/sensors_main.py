import time
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler

from src.sensors.sensor_benchmark import sonde_bench
from src.sensors.utils import end


def launch_sensors(isTest=False):
    # sonde1(isTest)
    # sonde2(isTest)
    # sonde3(isTest)
    # sonde4(isTest)
    # sonde5(isTest)
    # sonde7(isTest, isHorizontal=True)
    # sonde7(isTest, isHorizontal=False)
    # sonde9(isTest)
    # sonde10(isTest)
    # sonde12(isTest)
    # sonde14(isTest)
    # sonde15(isTest)
    # sonde16(isTest)
    # sonde13(isTest)
    scheduleYourSensors(BlockingScheduler())  # If you need actualized data :)


def addSchedule(scheduler, sonde, timeToRun=datetime.now(), second=8):
    scheduler.add_job(sonde, 'interval', seconds=second, next_run_time=timeToRun)


def scheduleYourSensors(scheduler):  # pragma: no cover
    localScheduler = scheduler
    now = datetime.now()
    # scheduler.add_job(sonde1, 'interval', seconds=2)
    # addSchedule(scheduler, sonde2, timeToRun=now + timedelta(milliseconds=100), second=40)
    # addSchedule(scheduler, sonde3, timeToRun=now + timedelta(milliseconds=200), second=62)
    # addSchedule(scheduler, sonde4, timeToRun=now + timedelta(milliseconds=300), second=19)
    # addSchedule(scheduler, sonde5, timeToRun=now + timedelta(milliseconds=400), second=16)
    # scheduler.add_job(sonde6, 'interval', seconds=45)
    # scheduler.add_job(sonde7, 'interval', seconds=35,
    #                   next_run_time=now + timedelta(milliseconds=500), args=[False, False])
    # scheduler.add_job(sonde7, 'interval', seconds=57,
    #                   next_run_time=now + timedelta(milliseconds=600), args=[False, True])
    # addSchedule(scheduler, sonde9, timeToRun=now + timedelta(milliseconds=700), second=39)
    # addSchedule(scheduler, sonde10, timeToRun=now + timedelta(milliseconds=800), second=50)
    # addSchedule(scheduler, sonde12, timeToRun=now + timedelta(milliseconds=900), second=45)
    # addSchedule(scheduler, sonde14, timeToRun=now + timedelta(milliseconds=150), second=34)
    # addSchedule(scheduler, sonde15, timeToRun=now + timedelta(milliseconds=250), second=28)
    # addSchedule(scheduler, sonde16, timeToRun=now + timedelta(milliseconds=350), second=30)
    #addSchedule(scheduler, sonde6, timeToRun=now, second=20)
    addSchedule(scheduler, sonde_bench, timeToRun=now + timedelta(milliseconds=350), second=30)
    print(f"(+) Tipboard starting schedul task", flush=True)
    scheduler.start()
    return True


def stopTheSensors(localScheduler):
    if localScheduler is not None:
        localScheduler.shutdown()


if __name__ == "__main__":  # pragma: no cover
    print(f"(+) Tipboard  sensors initialisation", flush=True)
    start_time = time.time()
    # launch_sensors()
    scheduleYourSensors(BlockingScheduler())  # If you need actualized data :)
    end(title="startUp", start_time=start_time)
