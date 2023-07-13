def toplama(*args):
    return sum(args)

numbers = []
while True:
    input_value = input("Bir sayı girin veya çıkmak için 'q' tuşuna basın: ")
    if input_value.isdigit():
        numbers.append(int(input_value))
    elif input_value == "q":
        break

print("Girilen sayılar:", numbers)
print("Toplam:", toplama(*numbers))
