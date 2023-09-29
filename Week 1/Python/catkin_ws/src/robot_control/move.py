from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="turtlebot")

a = robotcontrol.get_laser(360)
b = robotcontrol.get_laser(0)
c = robotcontrol.get_laser(719)

while a > 1:
    robotcontrol.move_straight()
    a = robotcontrol.get_laser(360)

else :
    robotcontrol.turn("clockwise", 9, 1)

robotcontrol.stop_robot()