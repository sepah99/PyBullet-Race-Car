import pybullet as p
import pybullet_data

# Can alternatively pass in p.DIRECT
# client = p.connect(p.GUI)
# p.setGravity(0, 0, -10, physicsClientId=client)
#
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# planeId = p.loadURDF("plane.urdf")
#
# carId = p.loadURDF("racecar/racecar.urdf", basePosition=[0,0,0.2])
# position, orientation = p.getBasePositionAndOrientation(carId)
#
#
# for _ in range(300):
#     pos, ori = p.getBasePositionAndOrientation(carId)
#     p.applyExternalForce(carId, 0, [50, 0, 0], pos, p.WORLD_FRAME)
#     p.stepSimulation()


# from time import sleep
#
# p.connect(p.GUI)
# p.loadURDF("simplecar.urdf")
# sleep(3)

import pybullet as p
import time
from time import sleep
p.connect(p.GUI)
p.setGravity(0, 0, -10)

angle = p.addUserDebugParameter('Steering', -0.5, 0.5, 0)
throttle = p.addUserDebugParameter('Throttle', -20, 20, 0)
acceleration = p.addUserDebugParameter('Acceleration', -2, 2, 0)
wheel_indices = [1, 3, 4, 5]
hinge_indices = [0, 2]
car = p.loadURDF('simplecar.urdf', [0, 0, 0.1])
plane = p.loadURDF('simpleplane.urdf')
user_angle = 0
user_throttle = 0
while True:
    # user_angle = p.readUserDebugParameter(angle)
    # user_throttle = p.readUserDebugParameter(throttle)

    # qKey = ord('q')
    # keys = p.getKeyboardEvents()
    # if qKey in keys and keys[qKey] & p.KEY_WAS_TRIGGERED:
    #     break;

    upKey = ord('w')
    downKey = ord('s')
    key = p.getKeyboardEvents()

    if upKey in key and key[upKey] & p.KEY_WAS_TRIGGERED:
        user_throttle += 1

    if downKey in key and key[downKey] & p.KEY_WAS_TRIGGERED:
        user_throttle -= 1

    leftKey = ord('a')
    rightKey = ord('d')
    if leftKey in key and key[leftKey] & p.KEY_WAS_TRIGGERED:
        user_angle -= 0.5
    elif rightKey in key and key[rightKey] & p.KEY_WAS_TRIGGERED:
        user_angle += 0.5

    accelKey = ord('q')
    deccelKey = ord('e')
    if deccelKey in key and key[deccelKey] & p.KEY_WAS_TRIGGERED:
        acceleration -= 0.5
    elif accelKey in key and key[accelKey] & p.KEY_WAS_TRIGGERED:
        acceleration += 0.5


    for joint_index in wheel_indices:
        p.setJointMotorControl2(car, joint_index,
                                p.VELOCITY_CONTROL,
                                targetVelocity=user_throttle)
    for joint_index in hinge_indices:
        p.setJointMotorControl2(car, joint_index,
                                p.POSITION_CONTROL,
                                targetPosition=user_angle)
    p.stepSimulation()


