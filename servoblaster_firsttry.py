import os
from time import sleep

while True:
  os.system('echo 1=180 > /dev/servoblaster')
  sleep(1)
  os.system('echo 1=2500us > /dev/servoblaster')
  sleep(1)
  os.system('echo 1=1000us > /dev/servoblaster')
  sleep(1)
  os.system('echo 1=2500us > /dev/servoblaster')
  sleep(1)
