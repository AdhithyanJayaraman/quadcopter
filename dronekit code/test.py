from dronekit import connect, VehicleMode, LocationGlobalRelative
# import dronekit_sitl
from time import sleep
# stil = dronekit_sitl.start_default()
# connection_string = stil.connection_string()
def arm_hover(alt):
    # quad = connect(connection_string, wait_ready=True)
    # quad = connect("/dev/ttyUSB0", wait_ready=False, baud=57600)
    quad = connect("udp:127.0.0.1:14560", wait_ready=False, heartbeat_timeout=180)
    quad.wait_ready(True, raise_exception=False)
    print("Basic pre-arm checks")
    # while not quad.is_armable:
    #     print(" Waiting for vehicle to initialise...")
    #     sleep(1)
    print ("Arming motors")
    
    quad.armed   = True
    while not quad.armed:
        quad.mode    = VehicleMode("GUIDED")
        quad.armed   = True
        print(" Waiting for arming...")
        sleep(1)
        print quad.mode
    sleep(2)
    print("Taking off!")
    
    while True:
        quad.simple_takeoff(alt)
        print(" Altitude: ", quad.location.global_relative_frame.alt)
        #Break and return from function just below target altitude.
        if quad.location.global_relative_frame.alt>=alt*0.95:
            print("Reached target altitude")
            break
        sleep(0.5)
    sleep(10)
    # quad.mode = VehicleMode("LAND")
    # while True:
    #     print(" Altitude: ", quad.location.global_relative_frame.alt)
    #     #Break and return from function just below target altitude.
    #     if quad.location.global_relative_frame.alt<=0.5:
    #         print("Reached target altitude")
    #         break
    #     sleep(0.5)
    # quad.close()

arm_hover(2)