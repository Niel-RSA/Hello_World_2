import platform
import socket
print("Hello World")
name = input("What is your name: ")
computer_name = str(socket.gethostname())
computer_name = str(platform.node())
print(f"Hello {name}")
print(f"My name is: {computer_name}")
