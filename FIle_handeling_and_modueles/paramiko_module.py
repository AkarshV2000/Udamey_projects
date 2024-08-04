import paramiko
ssh = paramiko.SSHClient()   # need to initae the ssh client

ssh.connect(hostname='201.444.123.222', username='akarverm', password= ' abc123') #connection to the remote server is made
stdin,stdout,stderr = ssh.exec_command("free -m") #running a command on the remote server
print(stdout.readlines()) # printing the out of that command
ssh.close() #closing the connection
