def square_list():
    s_liste =[]
    num1 = int(input("Enter the first number "))
    num2 = int(input("Enter the second number"))
    if num1 > num2:
        num1, num2 = num2, num1
    for i in range(num1,num2+1):
        s_liste.append(i**2)
    return s_liste

liste = square_list()
print(liste)