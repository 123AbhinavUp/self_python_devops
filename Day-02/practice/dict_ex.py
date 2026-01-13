info = {
    "Name": "Abhinav",
    "age" : 21,
    "state" : "UP",
    "weight": 78.5
}

#print(info)

info.update({"Work_Location":"Banglore"})
print(f"I live in",info["state"])

print(info)

#print(dir(info))  This dir function will tell u what u can achieve through the defined dict which is very helpful.

for i in info.keys():   # Print only keys of the defined dict
    print(i)

for i in info.values():  # Print only values of the defined dict
    print(i)

for i in info.items():  # Print both key-value pair of the defined dict
    print(i)

for key, value in info.items():
    print(key,value)