n = int(input("take value from user:"))

for i in range(n):
    env = input("Enter the enviroment: ")

    print("Enviroment variable given by user: ",env)

    #Conditional Statement simple else if
    if env == "prod":
        print("Don't deploy on Friday")

    elif env == "stg":
        print("Take backup and test well!")
    
    else:
        print("Safe to deploy on any day")