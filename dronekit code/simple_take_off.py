from dronekit import connect, VehicleMode, LocationGlobalRelative
# import dronekit_sitl
# stil = dronekit_sitl.start_default()
# connection_string = stil.connection_string()
#import gps
import time
# Connect to the Vehicle (in this case a simulator running the same computer)

vehicle = connect("/dev/ttyUSB0", wait_ready=False, baud = 57600)
vehicle.wait_ready(True, raise_exception=False)

# vehicle = connect(connection_string, wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """
    
    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    # while not vehicle.is_armable:
    #     print(" Waiting for vehicle to initialise...")
    #     time.sleep(1)
    print ("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.armed   = True
    vehicle.mode    = VehicleMode("GUIDED")
    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    vehicle.parameters['RTL_ALT']=0 #Return to Launch Altitute
    vehicle.airspeed = 3
    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        #Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
            print("Reached target altitude")
            break
        time.sleep(0.5)
    time.sleep(5)
    # lon = vehicle.location.global_relative_frame.lon
    # lon = lon+0.0005
    # lat = vehicle.location.global_relative_frame.lat
    # lat = lat+0.0005
    # print(lat,lon)
    # point = LocationGlobalRelative(lat,lon,aTargetAltitude)
    # vehicle.simple_goto(point)
    # while True:
    #     print(" Altitude: ", vehicle.location.global_relative_frame)
    #     if(vehicle.location.global_relative_frame.lon>=lon-0.0001):
    #         print("Point 1")
    #         break
    #     time.sleep(0.5)
    # vehicle.simple_goto(LocationGlobalRelative(lat-0.0005,lon-0.0005,aTargetAltitude))
    # while True:
    #     print(" Altitude: ", vehicle.location.global_relative_frame)
    #     if(vehicle.location.global_relative_frame.lon<=lon-0.0005+0.0001):
    #         print("Base")
    #         break
    #     time.sleep(0.5)
    # vehicle.simple_goto(LocationGlobalRelative(vehicle.location.global_relative_frame.lat,vehicle.location.global_relative_frame.lon,0.3))
    vehicle.mode = VehicleMode("RTL")
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if(vehicle.location.global_relative_frame.alt<=0.4):
            print("Landed")
            break
        # elif(vehicle.location.global_relative_frame.lon<=lon-0.0005+0.0001):
            # print("Base")
        time.sleep(0.5)
arm_and_takeoff(2)