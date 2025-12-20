# Take threshold value from the user
# Check the CPU utilization of your system and print the value on terminal
# If system utilization is more that threshold given by user. Send mail to user 
import psutil

def cpu_usage_check():
    user_threshold = int(input("Take threshold value from the user: "))

 # Get the CPU utilization over the last 1 second
    current_cpu_utilization = psutil.cpu_percent(interval=1)
    print(f"Current CPU utilization of system:",current_cpu_utilization)
    if current_cpu_utilization > user_threshold:
        print("Send a mail to user....")
    else:
        print("System is healthy....")


cpu_usage_check()

