"""file i/o"""
f=open("sam.txt","r")
# data=f.read()
# print(data)
# print(type(data))
lin1=f.readline()
print(lin1)
f.close()
import os
os.remove("sam.txt")
