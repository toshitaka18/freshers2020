import math
from message import Thanks_message

class Ev_car():
    def __init__(self, ev_wat):
        self.ev_wat = ev_wat

    def ev_charge(self):
        print(' ')
        print('{0}キロワット、充電しました。'.format(self.ev_wat))
        print('あなたの「J-chary」は、{0}km走ります。'.format(self.ev_wat * 1.5))
        if self.ev_wat <= 30:
            total_fee = math.floor(self.ev_wat * 17.33)
        elif self.ev_wat > 30 and self.ev_wat <= 80:
            total_fee = math.floor(self.ev_wat * 21.26)
        elif self.ev_wat > 80 and self.ev_wat <= 100:
            total_fee = math.floor(self.ev_wat * 24.07)
        else:
            total_fee = math.floor(self.ev_wat * 25.31)
        print('充電にかかった費用は、{0}円です。'.format(total_fee))
        print(Thanks_message.statment)