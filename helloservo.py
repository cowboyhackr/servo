import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

try:

	while True:
		p.ChangeDutyCycle(50)
		time.sleep(10)
		p.ChangeDutyCycle(12.5)
		time.sleep(10)
		p.ChangeDutyCycle(2.5)
		time.sleep(10)
		print datetime.datetime.now().time()

except KeyboardInterrupt:
	GPIO.cleanup()
