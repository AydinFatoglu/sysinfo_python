import tkinter as tk
import wmi
import platform
import socket
import datetime
import pyperclip

wmi_obj = wmi.WMI()
baseboard = wmi_obj.Win32_BaseBoard()[0]
computer_system = wmi_obj.Win32_ComputerSystem()[0]
system_enclosure = wmi_obj.Win32_SystemEnclosure()[0]
operating_system = wmi_obj.Win32_OperatingSystem()[0]
ip_address = socket.gethostbyname(socket.gethostname())
hostname = platform.node()
serial_number = baseboard.SerialNumber.strip()
user_name = computer_system.UserName
domain =   computer_system.Domain 
model_name = computer_system.SystemFamily
model_no =   computer_system.Model
system_serial_number = system_enclosure.SerialNumber.strip()
install_date_string = operating_system.InstallDate
install_date = datetime.datetime.strptime(install_date_string.split(".")[0], "%Y%m%d%H%M%S")

# Create a new window
root = tk.Tk()
root.title("BT DESTEK")

#center window
width = 420 # Width 
height = 290 # Height

screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
root.geometry(
'%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


# Add labels to display the system information
tk.Label(root, text="IP Address: " + ip_address, anchor='w').pack(fill='x')
tk.Label(root, text="Hostname: " + hostname, anchor='w').pack(fill='x')
tk.Label(root, text=f"Baseboard Serial Number: {serial_number}", anchor='w').pack(fill='x')
tk.Label(root, text=f"User Name: {user_name}", anchor='w').pack(fill='x')
tk.Label(root, text=f"Computer Domain: {domain}", anchor='w').pack(fill='x')
tk.Label(root, text=f"Model Name: {model_name}", anchor='w').pack(fill='x')
tk.Label(root, text=f"Model No: {model_no}", anchor='w').pack(fill='x')
tk.Label(root, text=f"System Serial Number: {system_serial_number}", anchor='w').pack(fill='x')
tk.Label(root, text=f"Windows Installation Date: {install_date}", anchor='w').pack(fill='x')

# Start the GUI event loop
root.mainloop()

