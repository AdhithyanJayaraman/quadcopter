# Quadcopter
## Precautions
1. Check motor sequence (found in Mission Planner>Initial Config>Optional Hardware>Motor Test)
2. Check motor rotation is as depicted in
http://ardupilot.org/copter/_images/motororder-quad-x-2d.png
3. **Pre Arms Checks Must be enabled** if Flying in Auto Modes
4. Set RTL(Return to Launch) Altitute as necessary default is 15m
5. First Test should be in Stabilize ie: Full mannual control
6. Land mode prevents disarm use RC to switch back to Stabilize
## Problems Faced
1. Flipping due to wrong motor sequence
2. Unexpected behaviour as Pre Arm Checks where turned off
3. RTL Altitude was set to default while testing in not so open area
4. Land Mode without GPS lock == Bad Idea
## MavROS Directory
It contains codes run using mavros
## Dronekit Directory
Contains codes run using dronekit
