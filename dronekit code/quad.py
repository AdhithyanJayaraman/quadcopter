from dronekit import connect, VehicleMode, LocationGlobalRelative
vehicle1 = connect("/dev/ttyUSB0", wait_ready=False, baud = 57600)
vehicle1.wait_ready(True, raise_exception=False)

vehicle2 = connect("/dev/ttyUSB1", wait_ready=False, baud = 57600)
vehicle2.wait_ready(True, raise_exception=False)
print vehicle2.mode.name
print vehicle1.mode.name
print vehicle1.location.global_relative_frame
while True:
    if(vehicle1.location.global_relative_frame.alt >= 0.5):
        print vehicle2.battery
    else:
        print vehicle1.location.global_relative_frame
        time.sleep(1)
#vehicle.close()
print "done"
