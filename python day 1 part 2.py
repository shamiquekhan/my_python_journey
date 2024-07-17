# chapter 2 
str="Welcome programmer . \nWE are creating it in python . "
print(str)
str2="let's start !!!"
print (str+str2) # sum of the strings
print(len(str2)) # lenght of thr string
print(str[2]) # indexing
print(str[0:7]) # slicing
print(str[8:len(str)])
print(str[:19]) #[0:19]
print(str[:-16]) # negetive slicing
# string functions
str3="i am Shamique"
# these functions dont work on existing str , rather create a new string
print(str3.endswith("e")) # true or false
print(str3.capitalize()) #capitalises 1st char
print(str3.replace("e","o")) # replace all occurence
print(str3.find("e")) # returns first index of 1 st occurence
print(str.count("a")) #count the occurence
# Conditional statement
a=10
b=20
c=15
if (a<=b):
    print('b is greter than a')
    if (c>=a):
        print('c is also greater than a') #nesting
elif (a==b):
    print("a and b are equal")
if (c>=a and c<=b):
    print("c is in between a and b") # two conditions used
else:
    print("a is greater than b")

