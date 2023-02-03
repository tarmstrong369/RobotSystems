from adc import ADC
class Sense():
    def __init__(self):
        self.ADC=ADC()
        self.read=ADC.read
        self.rv=ADC.read_voltage
        return [self.ADC,self.read,self.rv]
