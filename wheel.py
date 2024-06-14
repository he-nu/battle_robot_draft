from machine import Pin, PWM

class Wheel:
    def __init__(self, rpwm_pin, lpwm_pin, r_en_pin, l_en_pin, pwm_freq=1000, invert_speed=False):
        # Initialize the enable pins
        self.r_en = Pin(r_en_pin, Pin.OUT)
        self.l_en = Pin(l_en_pin, Pin.OUT)

        # Both of these need to be enabled to use the motor
        self.r_en.value(1)  # Set R_EN to high to enable
        self.l_en.value(1)  # Set L_EN to high to enable
        
        # Initialize the PWM pins
        self.rpwm = PWM(Pin(rpwm_pin), freq=pwm_freq)
        self.lpwm = PWM(Pin(lpwm_pin), freq=pwm_freq)

        self.invert_speed = invert_speed


    def set_speed(self, speed):
        if self.invert_speed:
            speed = -speed
            
        if speed > 0:
            self.rpwm.duty_u16(int(abs(speed) * 65535 / 100))
            self.lpwm.duty_u16(0)
        elif speed < 0:
            self.rpwm.duty_u16(0)
            self.lpwm.duty_u16(int(abs(speed) * 65535 / 100))
        else:
            self.rpwm.duty_u16(0)
            self.lpwm.duty_u16(0)

