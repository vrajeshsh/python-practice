'''To calculate time difference between two time inputs'''

print("To calculate time difference between two time inputs:")
hr_in = int(input("Enter Login hour: "))
min_in = int(input("Enter Login minute: "))
hr_out = int(input("Enter Logout hour: "))
min_out = int(input("Enter Logout minute: "))

if hr_in > hr_out:
 	hr_out+=24

time_in = (hr_in*60)+min_in
time_out = (hr_out*60)+min_out

diff = time_out-time_in

print("\nTime difference: ",diff//60," hour(s) ",(diff%60)," minute(s)",sep='')
