from machine import Pin
from time import sleep
from picozero import Servo
import network
import BlynkLib
servo=Servo(10)
ssid = 'Wifi Name'
password = 'Password'
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 
 
#wlan = network.WLAN(network.STA_IF)
#wlan.active(True)
#wlan.connect("Airtel_Ardent_5472","Ardent!132")
BLYNK_AUTH = 'Blynk Authentication Code'

"Connection to Blynk"
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
 
# Register virtual pin handler
@blynk.on("V0") #virtual pin V0
def v0_write_handler(value): #read the value
    if int(value[0]) == 1:
        servo.mid() #turn the led on        
    else:
        servo.min()    #tur
while True:
    #pir_state= pir.value()

        blynk.run()