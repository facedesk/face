from sense_hat import SenseHat
from time import sleep

class Face:
    def __init__(self):
        self.sense= SenseHat()
        self.test_all()
    def test_all(self):
        self.make_normal()
        sleep(0.5)
        self.make_happy()
        sleep(0.5)  
        self.make_sad()
        sleep(0.5)
	self.make_angry()
        sleep(0.5)
        self.sense.clear()
    def make_normal(self):
        e=(0,0,0)
        x=(200,200,200)#white
        face = [
            e,e,e,e,e,e,e,e,
            e,x,x,e,e,x,x,e,
            e,x,x,e,e,x,x,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,x,x,x,x,x,x,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
            ]
        self.sense.set_pixels(face)
    def make_happy(self):
        e=(0,0,0)
        x=(0,255,0)#green
        r=(255,0,0)#red
        face = [
            e,e,e,e,e,e,e,e,
            e,x,x,e,e,x,x,e,
            e,x,x,e,e,x,x,e,
            e,e,e,e,e,e,e,e,
            e,x,e,e,e,e,x,e,
            e,e,x,x,x,x,e,e,
            e,e,e,e,r,r,e,e,
            e,e,e,e,e,r,r,e
            ]
        self.sense.set_pixels(face)
    def make_sad(self):
        e=(0,0,0)
        x=(0,0,255)#blue
        face = [
            e,e,e,e,e,e,e,e,
            e,x,x,e,e,x,x,e,
            e,x,x,e,e,x,x,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,x,x,x,x,e,e,
            e,x,e,e,e,e,x,e,
            e,e,e,e,e,e,e,e
            ]
        self.sense.set_pixels(face)

    def make_angry(self):
        e=(0,0,0)
        w=(255,255,0)
        x=(255,0,0)#red
        face = [
            e,e,w,e,e,w,e,e,
            e,x,x,w,w,x,x,e,
            e,x,x,e,e,x,x,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,x,e,x,e,x,e,e,
            x,e,x,e,x,e,x,e,
            e,e,e,e,e,e,e,e
            ]
        self.sense.set_pixels(face)

if __name__=="__main__":
    F = Face()
    
    



