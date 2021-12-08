with open(file="devices.txt", mode="a") as f:
   while True:
       device_name = input('Add device with name or type "exit" to quit: ')
       if device_name.lower() == "exit":
           print("Exiting...")
           break
   else:
            f.write(device_name + "\n")