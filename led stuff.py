import pigpio
import time
pi = pigpio.pi()
data = 17

if not pi.connected():
    exit()
    
def on(data):
    pi.set_PWM_dutycycle(data,255)

def off(data):
    pi.set_PWM_dutycycle(data,0)

on(data)
time.sleep(1000)
pi.stop()
