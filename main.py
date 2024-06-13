import move_around
import time
import machine

def blink_led():
    led = machine.Pin('LED', machine.Pin.OUT)
    print("blinking led")
    for _ in range(3):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

def main():
    blink_led()
    move_around.main()





