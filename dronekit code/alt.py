#alitude readings
from dronekit import connect, VehicleMode, LocationGlobalRelative
from time import sleep
vehicle = connect("/dev/ttyUSB0", wait_ready=False, baud = 57600)
vehicle.wait_ready(True, raise_exception=False)

while True:
    print(vehicle.location.global_relative_frame.alt)
    sleep(0.4)