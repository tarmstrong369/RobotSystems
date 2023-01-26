from picarx_improved import Picarx
import timer
from datetime import datetime, timedelta

pcar= Picarx()

def Steering_Calib(): # Steering Calibration Check
    pcar.set_dir_servo_angle(0)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.forward(5)
    pcar.stop()

def forward_backward():
    pcar.set_dir_servo_angle(0)
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.forward(5)
    pcar.stop()
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.backward(5)


def Parallel_ParkR():
    pcar.Picarx.set_dir_servo_angle(20)
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.Picarx.backward(2)
    pcar.Picarx.stop()
    pcar.Picarx.set_dir_servo_angle(-40)
    end_time = datetime.now() + timedelta(seconds=4)
    while datetime.now() < end_time:
        pcar.Picarx.backward(3)
    pcar.Picarx.stop()
    pcar.Picarx.set_dir_servo_angle(20)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.Picarx.forward(3)
    pcar.Picarx.stop()

def Parallel_ParkL():
    pcar.Picarx.set_dir_servo_angle(-20)
    end_time = datetime.now() + timedelta(seconds=2)
    while datetime.now() < end_time:
        pcar.Picarx.backward(2)
    pcar.Picarx.stop()
    pcar.Picarx.set_dir_servo_angle(40)
    end_time = datetime.now() + timedelta(seconds=4)
    while datetime.now() < end_time:
        pcar.Picarx.backward(3)
    pcar.Picarx.stop()
    pcar.Picarx.set_dir_servo_angle(-20)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.Picarx.forward(3)
    pcar.Picarx.stop()

def K_Turn():
    pcar.Picarx.set_dir_servo_angle(-40)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.Picarx.forward(3)
    pcar.Picarx.stop()
    pcar.Picarx.set_dir_servo_angle(40)
    end_time = datetime.now() + timedelta(seconds=3)
    while datetime.now() < end_time:
        pcar.Picarx.backward(3)
    pcar.Picarx.stop()
    pcar.Picarx.set_dir_servo_angle(0)
    end_time = datetime.now() + timedelta(seconds=1)
    while datetime.now() < end_time:
        pcar.Picarx.backward(5)
    pcar.Picarx.stop()