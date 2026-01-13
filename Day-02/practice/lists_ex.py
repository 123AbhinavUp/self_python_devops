a = 100
b = [100, 2.5, "ibm", True]   # List ko define karne ka phela tarika
print(type(a))
print(type(b))
print(f"Value present in list: ", b)

c = list() # List ko define karne ka dusra tarika

print(type(c))

c.append("aws")
c.append("gcp")
c.append("azure")
c.append("oracle")
c.append("alibaba")

print(f"World leader for Cloud Service Provider:",c[0])
print(f"Other Cloud Service Providers:",c[-3])
print("Length of list c:",len(c))

print(dir(c)) # dir will tell u what are the things u can do with list

print(c.extend.__doc__) # This __doc__ will tell what we can achieve through the built-in function like append,count,index etc.
print(c.count.__doc__)

for cloud in c:
    if cloud == "aws":
        print(f"{cloud} is the world leader for Cloud Service Provider")
    elif cloud == "gcp":
        print(f"{cloud} is the 2nd largest Cloud Service Provider")
    else:
        print("Not covered")









