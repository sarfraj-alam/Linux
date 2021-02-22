import subprocess # This module is used to get the output of system commands like- date, cal etc.
import getpass # This function is similar to input function but this will not do echo back

original_psw  = "1234"

passwd = getpass.getpass("Enter the password : ")

if ( passwd != original_psw ) :
	print("Incorrect Password")
	exit()

else:
	cmd = input("Enter the command : ")
	x  = subprocess.getstatusoutput(cmd)
	status = x[0]
	cmd_output = x[1]
	
	if ( status == 0):
		print(cmd_output)
	else:
		print("Command Not Found")
