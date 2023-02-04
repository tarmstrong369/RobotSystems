from adc import ADC
from picarx_improved import Picarx

pcar=Picarx
class Sense(object):
    def __init__(self, pin0, pin1, pin2):
        self.chn_0 = ADC(pin0)
        self.chn_1 = ADC(pin1)
        self.chn_2 = ADC(pin2)
        return [ADC.read(self.chn_0), ADC.read(self.chn_1), ADC.read(self.chn_2)]

class Interp(object):
    def __init__(self,sensitivity,polarity):

class Control(object):
    def __init__(self, pos):
        if pos>0:
            steering_angle=-10
            pcar.turning(steering_angle)
        elif pos<0:
            steering_angle=10
            pcar.turning(steering_angle)
        elif pos==0:
            steering_angle=0
            pcar.turning(steering_angle)
        return steering_angle
