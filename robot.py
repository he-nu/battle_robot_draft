import time
from hcsr04 import HCSR04
from wheel import Wheel

class Robot:
    def __init__(self, left_wheel_pins, right_wheel_pins, weapon_wheel_pins, sensor_pins, default_speed=60):
        self.left_wheel = Wheel(
            rpwm_pin=left_wheel_pins['rpwm'], 
            lpwm_pin=left_wheel_pins['lpwm'], 
            r_en_pin=left_wheel_pins['r_en'], 
            l_en_pin=left_wheel_pins['l_en']
        )
        self.right_wheel = Wheel(
            rpwm_pin=right_wheel_pins['rpwm'], 
            lpwm_pin=right_wheel_pins['lpwm'], 
            r_en_pin=right_wheel_pins['r_en'], 
            l_en_pin=right_wheel_pins['l_en'], 
            invert_speed=True
        )
        self.weapon_wheel = Wheel(
            rpwm_pin=weapon_wheel_pins['rpwm'], 
            lpwm_pin=weapon_wheel_pins['lpwm'], 
            r_en_pin=weapon_wheel_pins['r_en'], 
            l_en_pin=weapon_wheel_pins['l_en']
        )
        
        self.front_sensor = HCSR04(trigger_pin=sensor_pins['front']['trigger'], echo_pin=sensor_pins['front']['echo'])
        self.right_sensor = HCSR04(trigger_pin=sensor_pins['right']['trigger'], echo_pin=sensor_pins['right']['echo'])
        self.left_sensor = HCSR04(trigger_pin=sensor_pins['left']['trigger'], echo_pin=sensor_pins['left']['echo'])
        self.b_right_sensor = HCSR04(trigger_pin=sensor_pins['back_right']['trigger'], echo_pin=sensor_pins['back_right']['echo'])
        self.b_left_sensor = HCSR04(trigger_pin=sensor_pins['back_left']['trigger'], echo_pin=sensor_pins['back_left']['echo'])
        
        self.default_speed = default_speed
    
    def stop(self):
        self.left_wheel.set_speed(0)
        self.right_wheel.set_speed(0)
    
    def move_forward(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.left_wheel.set_speed(speed)
        self.right_wheel.set_speed(speed)
    
    def move_backwards(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.left_wheel.set_speed(-speed)
        self.right_wheel.set_speed(-speed)
    
    def turn_left_inplace(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.right_wheel.set_speed(speed)
        self.left_wheel.set_speed(-speed)
    
    def turn_right_inplace(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.right_wheel.set_speed(-speed)
        self.left_wheel.set_speed(speed)
    
    def turn_left_around(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.right_wheel.set_speed(speed)
        self.left_wheel.set_speed(0)
    
    def turn_right_around(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.left_wheel.set_speed(speed)
        self.right_wheel.set_speed(0)
    
    def back_left(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.left_wheel.set_speed(-speed)
        self.right_wheel.set_speed(0)
    
    def back_right(self, speed=None):
        if speed is None:
            speed = self.default_speed
        self.right_wheel.set_speed(-speed)
        self.left_wheel.set_speed(0)
    
    def turn_r_180(self):
        turn_time = 2  # Adjust this value as needed
        self.stop()
        self.turn_right_inplace()
        time.sleep(turn_time)
        self.stop()
    
    def turn_l_180(self):
        turn_time = 2  # Adjust this value as needed
        self.stop()
        self.turn_left_inplace()
        time.sleep(turn_time)
        self.stop()
