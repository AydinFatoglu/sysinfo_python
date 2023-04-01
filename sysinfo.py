import wmi
import platform
import socket
import datetime

# create a WMI object to access the system information
wmi_obj = wmi.WMI()

# retrieve the first instance of the Win32_BaseBoard class
baseboard = wmi_obj.Win32_BaseBoard()[0]

# retrieve the first instance of the Win32_ComputerSystem class
computer_system = wmi_obj.Win32_ComputerSystem()[0]

# retrieve the first instance of the Win32_SystemEnclosure class
system_enclosure = wmi_obj.Win32_SystemEnclosure()[0]

# retrieve the first instance of the Win32_OperatingSystem class
operating_system = wmi_obj.Win32_OperatingSystem()[0]

# Get the local IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Get the computer hostname
hostname = platform.node()

# retrieve the serial number of the baseboard
serial_number = baseboard.SerialNumber.strip()

# retrieve the value of the UserName property
user_name = computer_system.UserName
domain =   computer_system.Domain 
model_name = computer_system.SystemFamily
model_no =   computer_system.Model

# retrieve the value of the SerialNumber property
system_serial_number = system_enclosure.SerialNumber.strip()

# retrieve the value of the InstallDate property
install_date_string = operating_system.InstallDate

# convert the InstallDate string to a datetime object
install_date = datetime.datetime.strptime(install_date_string.split(".")[0], "%Y%m%d%H%M%S")

# Display the information in a BGInfo-like format
print("IP Address: " + ip_address)
print("Hostname: " + hostname)
print(f"Baseboard Serial Number: {serial_number}")
print(f"User Name: {user_name}")
print(f"Computer Domain: {domain}")
print(f"Model Name: {model_name}")
print(f"Model No: {model_no}")
print(f"Sytem Serial Number: {system_serial_number}")
print(f"Windows Installation Date: {install_date}")





















