import os
import time

while True:
	os.system('sudo python /home/pi/lightshowpi/py/synchronized_lights.py')
	time.sleep(10)
