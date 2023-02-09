from sim_robot_hat import adc as ADC
from picarx_improved import Picarx

pcar=Picarx
class SenseGS():
    def __init__(self):
        self.chn_0 = ADC("A0").read()
        self.chn_1 = ADC("A1").read()
        self.chn_2 = ADC("A2").read()
        self.list=[]


    def sensorGS(self):
        self.list = [self.chn_0, self.chn_1, self.chn_2]
        return self.list

class InterpGS():
    def __init__(self):
        self.sensor = SenseGS()
        self.darklight = 800 #light/dark cutoff
        self.edgedet= 200 #detect edge
        self.vals = []
        self.edges = [0, 0]
        self.polar = [0, 0]
        self.intvals = ["", "", ""]

        def GSvals(self):
            self.vals = self.sensor.sensorGS()
            for i, val in enumerate(self.vals):
                if val >= self.darklight:
                    self.intals[i]="L" #light
                else:
                    self.intvals[i]="D" #dark

        def EdgesDetection(self):
            vals = self.vals
            if abs(vals[0]-vals[1])>=self.edgedet:
                self.edges[0]=abs(vals[0]-vals[1])
                self.polar[0]=int(vals[0]<vals[1])-int(vals[0]>vals[1])
            else:
                self.edges[0]=0
                self.polar[1]=0
            if abs(vals[1]-vals[2])>=self.edgedet:
                self.edges[1]=abs(vals[1]-vals[2])
                self.polar[1]=int(vals[2]<vals[1])-int(vals[2]>vals[1])
            else:
                self.edges[1]=0
                self.polar[1]=0
        def SelfCorrect(self):
            if self.polar[0]==self.polar[1]:
                return 0
            elif self.polar[0] < self.polar[1]:
                return -1*abs(self.edges[0]+self.edges[1])/(2*max(self.vals))
            elif self.polar[1] < self.polar[0]:
                return abs(self.edges[0]+self.edges[1])/(2*max(self.vals))

class Control():
    def __init__(self):

