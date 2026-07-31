import psutil

def check_system():
    print("System Health Report")
    print("--------------------")

    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

    memory = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory}%")

    disk = psutil.disk_usage('/').percent
    print(f"Disk Usage: {disk}%")

if __name__ == "__main__":
    check_system()