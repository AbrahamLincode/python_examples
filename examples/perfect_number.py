def perfect_nu():
    num = int(input("Please enter the number: "))
    divisors = []
    
    if num <= 0:
        print("Enter a POSITIVE INTEGER!")
        return 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    
    summ = sum(divisors)
    
    if summ == num:
        print("This number is PERFECT!")
        print("Divisors:", divisors)
    else:
        print("This number is NOT perfect.")
    
    return summ

perfect_nu()
