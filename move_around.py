from robot import Robot
import time
import pin_config as pc

        
def main():
    print("Executing main()")
    battle_robot = Robot(left_wheel_pins=pc.left_wheel_pins,
                     right_wheel_pins=pc.right_wheel_pins,
                     weapon_wheel_pins=pc.weapon_wheel_pins,
                     sensor_pins=pc.sensor_pins)
    print("Robot initialized")
    time.sleep(1)
    print("moving forwards")
    battle_robot.move_forward()
    time.sleep(3)
    print("moving backwards")
    battle_robot.move_backwards()
    time.sleep(3)
    count= 0
    print_sequence = 1
    while print_sequence <= 10:
        if count % 20 == 0:
            print(f"Sequence: {print_sequence}")
            print("\n")
            print(f"Front sensor {battle_robot.front_sensor.distance_cm()}")
            print(f"Left sensor {battle_robot.left_sensor.distance_cm()}")
            print(f"Right sensor {battle_robot.right_sensor.distance_cm()}")
            print(f"Back left {battle_robot.b_left_sensor.distance_cm()}")
            print(f"Back right {battle_robot.b_right_sensor.distance_cm()}")
            print("-------------------------------------------")
            print_sequence += 1
        count += 1
        try:
            battle_robot.move_forward()
            # if battle_robot.front_sensor.distance_cm() < 30:
            #    while battle_robot.front_sensor.distance_cm() < 100:
            #        if battle_robot.right_sensor.distance_cm() > battle_robot.left_sensor.distance_cm():
            #            battle_robot.turn_right_inplace()
            #        else:
            #            battle_robot.turn_left_inplace()
        except:
            return None
    print("Closing")
if __name__ == "__main__":
    main()
    

