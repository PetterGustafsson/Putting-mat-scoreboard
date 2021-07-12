
# measure = pot_value = pot.read()
# while True:
#   pot_value = pot.read()
#   if pot.read() < 0.5*measure:
#       print('BALL')
#       break
#   sleep(0.01)



import uos, machine
import gc
gc.collect()
import time
try:
  import usocket as socket
except:
  import socket
import network
import esp
esp.osdebug(None)
from machine import Pin, ADC
from time import sleep
import gc
gc.collect()

ssid = 'YOUR WIFI NETWORK' # Add wifi-manager
password = 'YOU WIFI PASSWORD'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass
print('Connection successful')
print(station.ifconfig())

switch = Pin(25, Pin.IN, Pin.PULL_UP)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       
red = Pin(32, Pin.OUT)
green = Pin(33, Pin.OUT)
green.value(0)
red.value(0)
