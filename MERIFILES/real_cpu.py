import psutil
#Return system CPU times as a named tuple
# print(psutil.cpu_percent(interval =1))
#interval = 1 means 1 sec

# you can have every usable function access through this 
# print(dir(psutil))

# this one will give you subprocess and doc in functiond
# print(psutil.subprocess.__doc__)

# for it in loop

threshold = float(input("Enter the threshold: "))
for i in range(10):
    if psutil.cpu_percent(interval=1) > threshold:
        print("cpu IS UNHEALTHY ")
    else:
        print(psutil.cpu_percent(interval=1))