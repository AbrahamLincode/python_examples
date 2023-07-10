num1 = int(input("Please enter the first number :"))
num2 = int(input("Please enter the second number"))

if num1 < num2 :                # Girilen sayıların büyüklüklerini kontrol etmek için if sayıların büyüklüklerini döngüde kullandığımız şekle evrilttik
    num1, num2 = num2, num1

ebob = 0
divisors = []
for test in range(num2,1,-1):
        if num2 % test ==0 and num1 % test ==0 :
            ebob = test
            divisors.append(ebob)

divisors.reverse()
print(ebob)
print(divisors)
