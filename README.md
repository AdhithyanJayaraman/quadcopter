# Quadcopter
## Precautions
1. Check motor sequence (found in Mission Planner>Initial Config>Optional Hardware>Motor Test)
2. Motor sequence of 1,2,3,4 is different from that of A,B,C,D in the sequence test
    * The sequence A,B,C,D corresponds to motors 1,4,3,2 respectively.
3. Check motor rotation is as depicted in
http://ardupilot.org/copter/_images/motororder-quad-x-2d.png
4. **Pre Arms Checks Must be enabled** if Flying in Auto Modes
5. Set RTL(Return to Launch) Altitute as necessary default is 15m
6. First Test should be in Stabilize ie: Full mannual control
7. Land mode prevents disarm use RC to switch back to Stabilize
8. If there is an issue with a motor or esc we can identify it by looking at the servo output **PWM** which will be **stuck on a particular value**
9. If the motor rpm is quite high it can be changed by changing the parameters **MOT_SPIN_MIN, MOT_SPIN_MAX and MOT_SPIN_ARM**

## Problems Faced
1. Flipping due to wrong motor sequence
2. Unexpected behaviour as Pre Arm Checks where turned off
3. RTL Altitude was set to default while testing in not so open area
4. Land Mode without GPS lock == Bad Idea
5. Unstable flight & crashes due to bad motor/esc

## Notes
* Take Off needs RC to be connected and above zero throttle
* Drifting in GPS Aided mode will be due to poor gps or no gps

## ROS Log
* tf seems like something we can use for following
* TODO: ROS on raspberry pi using ubuntu for arm servers

## Dronekit Log
* First Flight test caused drifting and altitute errors due to bad GPS
* Second Flight test extremely stable flight and altitude obtained after GPS 3D Fix
* TODO: Communication between drones

## MavROS Directory
It contains codes run using mavros

## Dronekit Directory
Contains codes run using dronekit
