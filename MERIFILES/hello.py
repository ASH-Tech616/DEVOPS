#its a case sensitve language

#int, str, float , str,boot
is_working =  True
print(type(is_working))


#list, tuple, dict ,set 


env = ["dev","stg", "prd"]     #this is a list of datas 
print(type(env))


#        DICTIONARY      behaves like an object of javascript
info = {
    "name" : "shubham",
    "years": 9.5,
    "env" : ["dev", "stg", "prd"]
}

#example oxford dictionary have key value pair
print(info["years"])    #this is a dictionary
print(type(info))



#a week days tuple of theses
#a tUPLE differs just because it is immutable and act as an array
days_of_week = ("mon","tue","wed", "thu", "fri","sat", "sun")
days_of_week[2]   #wed

# this is a set here ---->> it removes a duplicate in it
num = {0, 1, 1, 2,4, 5,7,8,9,7,7,7}
print(num)


