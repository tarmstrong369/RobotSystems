from picarx_improved import Picarx
import timer
from datetime import datetime, timedelta

pcar= Picarx()

def Steering_Calib(): # Steering Calibration Check
    pcar.set_dir_servo_angle(0)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.drive(5)
    pcar.stop()

def forward_backward():
    pcar.set_dir_servo_angle(0)
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.drive(5)
    pcar.stop()
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.drive(-5)


def Parallel_ParkR():
    pcar.turning(20)
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.drive(-2)
    pcar.stop()
    pcar.turning(-40)
    end_time = datetime.now() + timedelta(seconds=4)
    while datetime.now() < end_time:
        pcar.drive(-3)
    pcar.stop()
    pcar.turning(20)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.drive(3)
    pcar.stop()

def Parallel_ParkL():
    pcar.turning(-20)
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.drive(-2)
    pcar.stop()
    pcar.turning(40)
    end_time = datetime.now() + timedelta(seconds=4)
    while datetime.now() < end_time:
        pcar.drive(-3)
    pcar.stop()
    pcar.turning(-20)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.drive(3)
    pcar.stop()

def K_Turn():
    pcar.turning(-40)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.drive(3)
    pcar.stop()
    pcar.turning(40)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.drive(-3)
    pcar.stop()
    pcar.turning(0)
    end_time = datetime.now() + timedelta(seconds=1)
    while datetime.now() < end_time:
        pcar.drive(-5)
    pcar.stop()