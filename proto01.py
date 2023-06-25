import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import ctypes
import webbrowser
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





# Get the monitor size
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Create the main window
root = ctk.CTk()

# Set the window size to match the monitor size
root.geometry(f"{screen_width}x{screen_height}")

# Create a scrollable canvas
canvas = ctk.CTkCanvas(root)
canvas.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Create a frame inside the canvas to hold the containers
container_frame = tk.Frame(canvas)
container_frame.pack(pady=(screen_height // 2), anchor=tk.CENTER)

# Create a scrollbar for the canvas
scrollbar = ctk.CTkScrollbar(canvas, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to scroll with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=container_frame, anchor=tk.CENTER)

# Configure the canvas to expand with the window size
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Container data (image, buttons, and labels)
container_data = [
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/gimp.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "GIMP",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/blender.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "Blender",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/inkscape.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "Inkscape",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/krita.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "Krita",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/7-zip.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "7-Zip",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/Audacity.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "Audacity",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/Natron.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "Natron",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/shotcut.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "Shotcut",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/OpenToonz.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "OpenToonz",
    },
    {
        "image_path": "c:/Users/admin/Desktop/asset/images/scribus.png",
        "button_texts": ["install", "uninstall", "update"],
        "label_text": "Scribus",
    },
    # Add your container data here
]

# Define the grid dimensions
rows = len(container_data)
columns = 3

# Functions for install, uninstall, and update
def install_software(software_name):
    # Replace with your installation logic
    print(f"Installing {software_name}...")

def uninstall_software(software_name):
    # Replace with your uninstallation logic
    print(f"Uninstalling {software_name}...")

def update_software(software_name):
    # Replace with your update logic
    print(f"Updating {software_name}...")

# Create the units (containers)
for index, data in enumerate(container_data):
    # Create a container frame for each unit
    container = tk.Frame(container_frame, width=150, height=200, borderwidth=1, relief=tk.RAISED)
    container.grid(row=index // columns, column=index % columns, padx=5, pady=5)

    # Load the image
    image_path = data["image_path"]
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize the image as needed
    image = ImageTk.PhotoImage(image)

    # Create an image label
    image_label = ctk.CTkLabel(container, image=image)
    image_label.pack()

    # Create buttons
    buttons = []
    common_link = "https://www.example.com"  # Replace with your desired common link
    for button_text in data["button_texts"]:
        def open_link(link):
            webbrowser.open(link)

        if button_text == "install":
            button = ctk.CTkButton(container, text=button_text, command=lambda software=data["label_text"]: install_software(software))
        elif button_text == "uninstall":
            button = ctk.CTkButton(container, text=button_text, command=lambda software=data["label_text"]: uninstall_software(software))
        elif button_text == "update":
            button = ctk.CTkButton(container, text=button_text, command=lambda software=data["label_text"]: update_software(software))
        else:
            button = ctk.CTkButton(container, text=button_text, command=lambda link=common_link: open_link(link))
        
        button.pack(side="top", padx=1, pady=1)
        buttons.append(button)

    # Create a label
    label_text = data["label_text"]
    label = ctk.CTkLabel(container, text=label_text)
    label.pack(pady=10)

    # Save the widgets in the container as attributes for future reference
    container.buttons = buttons
    container.label = label
    container.image_label = image_label

    # Set the image as an attribute of the image label for reference
    image_label.image = image

# Update the canvas scroll region
container_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

# Configure the canvas to scroll with the mouse wheel
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind("<MouseWheel>", on_mouse_wheel)

# Bottom navigation bar
navbar_frame = tk.Frame(root)
navbar_frame.pack(side=tk.BOTTOM, pady=10)

# Tutorial window
def open_tutorial():
    webbrowser.open("https://frozecrate.000webhostapp.com/tutorial.html")

tutorial_button = ctk.CTkButton(navbar_frame, text="Tutorial", command=open_tutorial)
tutorial_button.pack(side=tk.LEFT, padx=10, pady=5)

# Credit window
def open_credit():
    credit_window = ctk.CTk()
    credit_window.title("Credits")
    

    credit_label = ctk.CTkLabel(credit_window, text="Your credits text here")
    credit_label.pack(padx=20, pady=10)

    credit_window.mainloop()

credit_button = ctk.CTkButton(navbar_frame, text="Credits", command=open_credit)
credit_button.pack(side=tk.LEFT, padx=10, pady=5)

# Run the custom Tkinter event loop
root.mainloop()
