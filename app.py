import RPi.GPIO as GPIO
from subprocess import call
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(18,GPIO.IN)
log=open('pylog2','w')
while True:
	if GPIO.input(14):
		call(['omxplayer', '/home/pi/ttf/lab.mp4'], stdout=f)
	if GPIO.input(15):
		call(['omxplayer', '/home/pi/ttf/startup.mp4'], stdout=f)
	if GPIO.input(18):
		call(['omxplayer', '/home/pi/ttf/pi.mp4'], stdout=f)

