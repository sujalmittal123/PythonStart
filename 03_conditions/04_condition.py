# You're building a smart thermostat alert system:
# If the device_status is "active"
# And temperature > 35 → Warn: "High temperature alert!"
# Else: "Temperature normal"
# If device is off "Device is offline"

devise_status = input(" enter the devise status sctive/or off: ").lower()
temperature = 38

if devise_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature normal")
else:
    print("Device is offline")
