import getpass
import os
import socket

user=getpass.getuser()
home=os.environ["HOME"]
host = socket.gethostname()

print( "user = {}".format(user))
print("home = {}".format(home))
print("host ={}".format(host))