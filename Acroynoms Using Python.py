
str1 = input("Enter the line which u wanted go for Acrnomys  ")
list1 = list(str1.split(" "))
s = ""
for i in list1:
    s+=i[0].upper()
print(s)
