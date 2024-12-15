

#List
print("\n--------------------")
print("*****LISTS*****")
environments = ["dev","prd","stg","test","dep"]
print("Length of environments",len(environments))
print(environments)
print("environmets 2nd element is ",environments[2])
add = input("Enter environments element to be added:")
environments.append(add)
print(environments)
print("--------------------\n")

#Dictionaries
device_info = {
    "device" : "windows",
    "RAM": 16,
    "Nvidia": True
}

print("\n--------------------")
print("*****Dictionaries*****")
print(device_info)
add_dict = int(input("Enter Value to be added to dictionary - Storage: (NUMBER)}"))
device_info.update({"Storage":add_dict})
print(device_info)
print("--------------------\n")

#Sets
print("\n--------------------")
print("*****SETS*****")
sets = {1,2,2,2,3,3,4,5,6}
print(sets)
print("--------------------\n")

#TUPLES
print("\n--------------------")
print("*****TUPLES*****")
days_of_week = ("mon","tue")
print(f"Days of week are {days_of_week}")
print(f"First Day of week is {days_of_week[0]}")
print("--------------------\n")


#ARRAYS
