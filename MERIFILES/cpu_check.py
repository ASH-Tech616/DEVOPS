cpu = float(input("Enter the CPU: "))# take input from the users

##conditionals
if cpu > 50:
    print("CPU OVER LOAD")

elif cpu > 20 and cpu < 50:   # in python and == || of c++
    print("send alarm")
else:
    print("cpu normal")


# we will install the psutils for a real cpu check in which python could access our real computer directory to check the cpu performance 
