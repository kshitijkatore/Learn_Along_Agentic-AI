device_status = "active"
temperature = 38

if device_status =="active":
    if temperature >35:
        print("High temprature alert!")
    else:
        print("Temprature is normal.")
else:
    print("Device is offline.")