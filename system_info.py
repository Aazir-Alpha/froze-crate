import platform
import psutil
import wmi

# Create a connection to WMI
conn = wmi.WMI()

# Open the text file in write mode
with open('sysverinfo/system_info.txt', 'w') as file:

    # CPU information
    cpu_info = conn.Win32_Processor()[0]
    file.write("CPU Information:\n")
    file.write(f"Name: {cpu_info.Name}\n")
    file.write(f"Manufacturer: {cpu_info.Manufacturer}\n")
    file.write(f"Max Clock Speed: {cpu_info.MaxClockSpeed} MHz\n")
    file.write(f"Number of Cores: {cpu_info.NumberOfCores}\n")
    file.write(f"Number of Logical Processors: {cpu_info.NumberOfLogicalProcessors}\n")

    # Memory information
    mem_info = psutil.virtual_memory()
    file.write("\nMemory Information:\n")
    file.write(f"Total: {round(mem_info.total / (1024 ** 3), 2)} GB\n")
    file.write(f"Available: {round(mem_info.available / (1024 ** 3), 2)} GB\n")
    file.write(f"Used: {round(mem_info.used / (1024 ** 3), 2)} GB\n")

    # Disk information
    disk_info = conn.Win32_LogicalDisk(DriveType=3)
    file.write("\nDisk Information:\n")
    for disk in disk_info:
        file.write(f"Drive: {disk.Caption}\n")
    disk_info = psutil.disk_usage("/")
    file.write(f"Total: {round(disk_info.total / (1024 ** 3), 2)} GB\n")
    file.write(f"Used: {round(disk_info.used / (1024 ** 3), 2)} GB\n")
    file.write(f"Free: {round(disk_info.free / (1024 ** 3), 2)} GB\n")

    # GPU information
    gpu_info = conn.Win32_VideoController()[0]
    file.write("\nGPU Information:\n")
    file.write(f"Name: {gpu_info.Name}\n")
    file.write(f"Adapter RAM: {round(int(gpu_info.AdapterRAM) / (1024 ** 3), 2)} GB\n")

    # Operating System information
    os_info = conn.Win32_OperatingSystem()[0]
    file.write("\nOperating System Information:\n")
    file.write(f"Caption: {os_info.Caption}\n")
    file.write(f"Version: {os_info.Version}\n")
    file.write(f"Build Number: {os_info.BuildNumber}\n")
