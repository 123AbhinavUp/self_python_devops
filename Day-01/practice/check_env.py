# Get the enviroment from user and print it

env = input("Enter the enviroment: ")

print("Enviroment variable given by user: ",env)

#Conditional Statement simple else if
if env == "prod":
    print("Don't deploy on Friday")

elif env == "stg":
    print("Take backup and test well!")
   
else:
    print("Safe to deploy on any day")


#Type Casting - Conversion of 1 data type to another

a = int(input("Enter the value of a"))
b = float(input("Enter the value of b"))

print("Addition of a & b:",a+b)
print("Sub of a & b:",a-b)
print("Multiple of a & b:",a*b)
print("Division of a & b:",a/b)