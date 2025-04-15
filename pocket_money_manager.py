print("hello sir")
print("sir please tell me your name" )
name = input("enter your name :")
print("hello",name,"sir")
print("sir can u tell me your daily expense")
expense = int(input("enter your expense: "))
monthlyexpense = expense * 30
print("your monthly expense is ",monthlyexpense )
print("sir how many holidays u have taken in this month?")
holidays = int(input("enter number of holidays u have taken "))
totalsum = monthlyexpense - holidays*expense
print("your total expense is ", totalsum)

#print("how much money ur parents gave u?")
#parentsgave = int(input("enter the pocketmoney "))

#moneyremaind = parentsgave +totalsum
#print("money in your pocket ",moneyremaind)
