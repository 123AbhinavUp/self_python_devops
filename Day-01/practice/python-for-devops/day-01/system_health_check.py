import psutil

def system_health_check():
    cpu_threshold = int(input("Take the CPU threshold value from user: "))
    mem_threshold = int(input("Take the mem threshold value from the user: "))
    disk_threshold = int(input("Take the disk threshold from the user: "))

    current_cpu_usage = psutil.cpu_percent(interval=1)
    current_mem_usage = psutil.virtual_memory().percent
    current_disk_usage = psutil.disk_usage('/').percent
    
    print(f"\nCPU Usage: {current_cpu_usage}%")
    print(f"Memory Usage: {current_mem_usage}%")
    print(f"Disk Usage: {current_disk_usage}%\n")


    if current_cpu_usage > cpu_threshold:
        print("Alert: CPU utilization is more than threshold!")
    else:
        print("Info: CPU utilization is under threshold!")
    
    if current_disk_usage > disk_threshold:
        print("Alert: Disk usage is more than threshold!")
    else:
        print("Info: Disk utilization is under threshold!")
    
    if current_mem_usage > mem_threshold:
        print("Alert: Memory utilization is more than threshold!")
    else:
        print("Alert: Memory utilizationis under threshold!")

system_health_check()
