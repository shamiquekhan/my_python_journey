m1=input("enter 1st movie")
m2=input("enter 2nd movie")
m3=input("enter 3rd movie")
l1=[]
l1.append(m1)
l1.append(m2)
l1.append(m3)
print("your favroite movies are :" , l1)
 # second methord
movies=[]
movies.append(input("enter your 1st fav movies : "))
movies.append(input("enter your 2nd fav movies : "))
movies.append(input("enter your 3rd fav movies : "))
print(movies)

"""palidrome"""
list=[12,23,34,23,12]
list2=list.copy()
list2.reverse()
if (list == list2) :
    print('this list is palindrome')
else:
    print("this list is not palindrome")
